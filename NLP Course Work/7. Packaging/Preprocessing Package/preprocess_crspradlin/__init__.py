from preprocess_crspradlin import utils

__version__ = '0.0.1'

def get_word_count(x):
    return utils._get_word_count(x)

def get_char_count(x):
    return utils._get_char_count(x)

def get_avg_wordlength(x):
    return utils._get_avg_wordlength(x)

def get_stopword_count(x):
    return utils._get_stopword_count(x)

def get_hashtag_count(x):
    return utils._get_hashtag_count(x)

def get_mention_count(x):
    return utils._get_mention_count(x)

def get_digit_count(x):
    return utils._get_digit_count(x)

def get_uppercase_word_count(x):
    return utils._get_uppercase_word_count(x)

def get_contraction_to_expansion(x):
    return utils._get_contraction_to_expansion(x)

def get_emails(x):
    return utils._get_emails(x)

def remove_emails(x):
    return utils._remove_emails(x)

def get_urls(x):
    return utils._get_urls(x)

def remove_urls(x):
    return utils._remove_urls(x)

def remove_rt(x):
    return utils._remove_rt(x)

def remove_special_chars(x):
    return utils._remove_special_chars(x)

def remove_html_tags(x):
    return utils._remove_html_tags(x)

def remove_accented_chars(x):
    return utils._remove_accented_chars(x)

def remove_stopwords(x):
    return utils._remove_stopwords(x)

def convert_to_base(x):
    return utils._convert_to_base(x)

def get_word_freq(df, col_nm):
    return utils._get_word_freq(df, col_nm)

def remove_common_words(x, word_freq, n=20):
    return utils._remove_common_words(x, word_freq, n)

def remove_rare_words(x, word_freq, n=20):
    return utils._remove_rare_words(x, word_freq, n)

def spelling_correction(x):
    return utils._spelling_correction(x)
