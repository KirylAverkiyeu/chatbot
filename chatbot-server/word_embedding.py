import globals


def embed(lemma):
    return(globals.tfidf.transform([lemma]).toarray())
