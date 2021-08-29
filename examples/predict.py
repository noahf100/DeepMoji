# -*- coding: utf-8 -*-

""" Use DeepMoji to score texts for emoji distribution.

The resulting emoji ids (0-63) correspond to the mapping
in emoji_overview.png file at the root of the DeepMoji repo.

Writes the result to a csv file.
"""

import argparse
import example_helper
import json
import csv
import numpy as np
from deepmoji.sentence_tokenizer import SentenceTokenizer
from deepmoji.model_def import deepmoji_emojis
from deepmoji.global_variables import PRETRAINED_PATH, VOCAB_PATH, EMOJI_MAPPINGS


parser = argparse.ArgumentParser(description='Inference on text.')
parser.add_argument('text', metavar='t', type=str,
                    help='Text to turn into emoji.')
args = parser.parse_args()
text = args.text


def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]


maxlen = 30
batch_size = 32

print('Tokenizing using dictionary from {}'.format(VOCAB_PATH))
with open(VOCAB_PATH, 'r') as f:
    vocabulary = json.load(f)
st = SentenceTokenizer(vocabulary, maxlen)
tokenized, _, _ = st.tokenize_sentences([text])

print('Loading model from {}.'.format(PRETRAINED_PATH))
model = deepmoji_emojis(maxlen, PRETRAINED_PATH)
model.summary()

print('Running predictions.')
prob = model.predict(tokenized)

# Find top emojis for each sentence. Emoji ids (0-63)
# correspond to the mapping in emoji_overview.png
# at the root of the DeepMoji repo.
scores = []
t_tokens = tokenized[0]
t_score = [text]
t_prob = prob[0]
ind_top = top_elements(t_prob, 5)
t_score.append(sum(t_prob[ind_top]))
# Convert to emoji
t_score.extend([EMOJI_MAPPINGS[i] for i in ind_top])
t_score.extend([t_prob[ind] for ind in ind_top])
scores.append(t_score)
print(t_score)
