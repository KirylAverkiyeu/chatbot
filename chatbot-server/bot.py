import text_normalization
import word_embedding
import cosine_similarity
import globals

globals.init()


def chat_tfidf(question):
    answer = text_normalization.text_normalization(question)
    answer = word_embedding.embed(answer)
    answer = cosine_similarity.cos_similarity(answer)
    return answer
