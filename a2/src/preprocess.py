import string
from underthesea import word_tokenize


def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation + '’' + '‘'))


def preprocess(s):
    s = s.strip()
    s = ' '.join(s.split())
    # s = remove_punctuation(s)
    s = word_tokenize(s, format='text')
    return s
