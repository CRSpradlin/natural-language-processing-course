import re
import os
import sys

import pandas as pd
import numpy as np
import spacy

from spacy.lang.en.stop_words import STOP_WORDS as stopwords

from bs4 import BeautifulSoup

import unicodedata

from textblob import TextBlob

nlp = spacy.load('en_core_web_sm')

def _get_word_count(x):
    return len(str(x).split())

def _get_char_count(x):
    s = x.split()
    s = ''.join(s)
    return len(s)

def _get_avg_wordlength(x):
    return _get_char_count(x)/_get_word_count(x)

def _get_stopword_count(x):
    return len([word for word in x.split() if word in stopwords])

def _get_hashtag_count(x):
    return len([word for word in x.split() if word.startswith('#')])

def _get_mention_count(x):
    return len([word for word in x.split() if word.startswith('@')])

def _get_digit_count(x):
    return len([digit for digit in x.split() if digit.isdigit()])

def _get_uppercase_word_count(x):
    return len([word for word in x.split() if word.isupper()])

def _get_contraction_to_expansion(x):
    contractions = {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "can't've": "cannot have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'd've": "he would have",
        "he'll": "he will",
        "he'll've": "he will have",
        "he's": "he is",
        "how'd": "how did",
        "how'd'y": "how do you",
        "how'll": "how will",
        "how's": "how does",
        "i'd": "i would",
        "i'd've": "i would have",
        "i'll": "i will",
        "i'll've": "i will have",
        "i'm": "i am",
        "i've": "i have",
        "isn't": "is not",
        "it'd": "it would",
        "it'd've": "it would have",
        "it'll": "it will",
        "it'll've": "it will have",
        "it's": "it is",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "mightn't've": "might not have",
        "must've": "must have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "needn't": "need not",
        "needn't've": "need not have",
        "o'clock": "of the clock",
        "oughtn't": "ought not",
        "oughtn't've": "ought not have",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "shan't've": "shall not have",
        "she'd": "she would",
        "she'd've": "she would have",
        "she'll": "she will",
        "she'll've": "she will have",
        "she's": "she is",
        "should've": "should have",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "so've": "so have",
        "so's": "so is",
        "that'd": "that would",
        "that'd've": "that would have",
        "that's": "that is",
        "there'd": "there would",
        "there'd've": "there would have",
        "there's": "there is",
        "they'd": "they would",
        "they'd've": "they would have",
        "they'll": "they will",
        "they'll've": "they will have",
        "they're": "they are",
        "they've": "they have",
        "to've": "to have",
        "wasn't": "was not",
        "u": " you ",
        "ur": " your ",
        "n": " and ",
        "won't": "would not",
        'dis': 'this',
        'bak': 'back',
        'brng': 'bring'
    }

    words = x.split()
    for index, word in enumerate(words):
        lower = str(word).lower()
        if lower in contractions:
            words[index] = contractions[lower]

    return ' '.join(words)

def _get_emails(x):
    emails = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', x)
    count = len(emails)

    return count, emails

def _remove_emails(x):
    return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', '', x)

def _get_urls(x):
    urls = re.findall(r'\S+://\S+', x)
    count = len(urls)

    return count, urls

def _remove_urls(x):
    return re.sub(r'\S+://\S+', '', x)

def _remove_rt(x):
    return re.sub(r'rt ', '', x)

def _remove_special_chars(x):
    x = re.sub(r'[^\w\s]+', '', x) # remove special characters
    x = ' '.join(x.split()) # remove extra spaces
    return x

def _remove_html_tags(x):
    return BeautifulSoup(x, 'lxml').get_text().strip()

def _remove_accented_chars(x):
    return unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore') # Normal Form Compose and Decompose

def _remove_stopwords(x):
    return ' '.join([t for t in x.split() if t not in stopwords])

def _convert_to_base(x):
    base_list = []
    doc = nlp(x)

    for token in doc:
        lemma = token.lemma_

        if lemma == '-PRON-' or lemma == 'be':
            lemma = token.text

        base_list.append(lemma)

    return ' '.join(base_list)

def _remove_common_words(x, n = 20):
    x = x.split()
    word_freq = pd.Series(x).value_counts()
    fn = word_freq[:n]

    return ' '.join([t for t in x.split() if t not in fn])

def _remove_rare_words(x, n = 20):
    x = x.split()
    word_freq = pd.Series(x).value_counts()
    fn = word_freq.tail(n)

    return ' '.join([t for t in x.split() if t not in fn])

def _spelling_correction(x):
    return TextBlob(x).correct()