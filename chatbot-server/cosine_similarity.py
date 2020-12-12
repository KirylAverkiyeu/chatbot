from sklearn.metrics import pairwise_distances  # for performing cosine similarity
import numpy as np
import random
import globals


def cos_similarity(tf):
    # applying cosine similarity
    cos = 1-pairwise_distances(globals.df_tfidf, tf, metric='cosine')
    # index_value=cos.argmax() # getting index value
    index_value = getIndex(cos)
    return globals.df['Text Response'].loc[index_value]


def getIndex(arr):
    indexes = []
    i = 0
    maxIdx = arr.argmax()
    for element in arr:
        if(element == arr[maxIdx]):
            indexes.append(i)
        i += 1
    if (len(indexes) == 0):
        return maxIdx
    return(random.choice(indexes))
