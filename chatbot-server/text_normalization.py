import re
import nltk
from nltk import word_tokenize  # for creating tokens
from nltk.stem import wordnet  # lemmatization
from nltk import pos_tag  # parts of speech


def text_normalization(dataset):
    text = str(dataset).lower()  # convert input to lowercase
    # exclude special characters, etc.
    spl_char_text = re.sub(r'[^a-z0-9]', ' ', text)
    tokens = nltk.word_tokenize(spl_char_text)  # word tokenizing
    lemma = wordnet.WordNetLemmatizer()  # initialize Lemmatizer
    # the parts of speech of every word
    tags_list = pos_tag(tokens, tagset=None)
    lemma_words = []
    for token, pos_token in tags_list:
        if pos_token.startswith('V'):  # verb
            pos_val = 'v'
        elif pos_token.startswith('J'):  # adjective
            pos_val = 'a'
        elif pos_token.startswith('R'):  # adverb
            pos_val = 'r'
        else:
            pos_val = 'n'  # noun
        lemma_token = lemma.lemmatize(token, pos_val)  # perform lemmatization
        lemma_words.append(lemma_token)  # append lemmatized token into a list
    return (" ".join(lemma_words))  # return lemmatized tokens as a sentence
