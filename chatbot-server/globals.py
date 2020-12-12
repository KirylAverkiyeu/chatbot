import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer  # tfid
import text_normalization


def init():
    global df
    df = pd.read_excel('bot_dialogue.xlsx')
    # fill the null value with the previous value
    df.ffill(axis=0, inplace=True)
    df['lemmatized_text'] = df['Context'].apply(
        text_normalization.text_normalization)
    global tfidf
    tfidf = TfidfVectorizer()  # initializing tfidf
    x_tfidf = tfidf.fit_transform(df['lemmatized_text']).toarray()
    global df_tfidf
    df_tfidf = pd.DataFrame(x_tfidf, columns=tfidf.get_feature_names())
