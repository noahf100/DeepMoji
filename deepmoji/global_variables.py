""" Global variables.
"""
import tempfile
from os.path import abspath, dirname

# The ordering of these special tokens matter
# blank tokens can be used for new purposes
# Tokenizer should be updated if special token prefix is changed
SPECIAL_PREFIX = 'CUSTOM_'
SPECIAL_TOKENS = ['CUSTOM_MASK',
                  'CUSTOM_UNKNOWN',
                  'CUSTOM_AT',
                  'CUSTOM_URL',
                  'CUSTOM_NUMBER',
                  'CUSTOM_BREAK']
SPECIAL_TOKENS.extend(['{}BLANK_{}'.format(SPECIAL_PREFIX, i)
                      for i in range(6, 10)])

ROOT_PATH = dirname(dirname(abspath(__file__)))
VOCAB_PATH = '{}/model/vocabulary.json'.format(ROOT_PATH)
PRETRAINED_PATH = '{}/model/deepmoji_weights.hdf5'.format(ROOT_PATH)

WEIGHTS_DIR = tempfile.mkdtemp()

NB_TOKENS = 50000
NB_EMOJI_CLASSES = 64
FINETUNING_METHODS = ['last', 'full', 'new', 'chain-thaw']
FINETUNING_METRICS = ['acc', 'weighted']

EMOJI_MAPPINGS = {
    0: '😂',
    1: '😒',
    2: '😩',
    3: '😭',
    4: '😍',
    5: '😔',
    6: '👌',
    7: '☺️',
    8: '❤️',
    9: '😏',
    10: '😁',
    11: '🎶',
    12: '😳',
    13: '💯',
    14: '😴',
    15: '😌',
    16: '😊',
    17: '🙌',
    18: '💕',
    19: '😑',
    20: '😅',
    21: '🙏',
    22: '😕',
    23: '😘',
    24: '❤️',
    25: '😐',
    26: '💁‍♀️',
    27: '😞',
    28: '🙈',
    29: '😫',
    30: '✌️',
    31: '😎',
    32: '😡',
    33: '👍',
    34: '😢',
    35: '😪',
    36: '😋',
    37: '😤',
    38: '🤚',
    39: '😷',
    40: '👏',
    41: '👀',
    42: '🔫',
    43: '😩',
    44: '😈',
    45: '😓',
    46: '💔',
    47: '♡',
    48: '🎧',
    49: '🙊',
    50: '😉',
    51: '💀',
    52: '😖',
    53: '😄',
    54: '😜',
    55: '😠',
    56: '🙅‍♀️',
    57: '💪',
    58: '👊',
    59: '💜',
    60: '💖',
    61: '💙',
    62: '😬',
    63: '✨',
}
