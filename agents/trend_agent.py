from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def analyze_trends(documents, top_k=10):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(2, 3),   # phrases instead of single words
        max_features=1000
    )

    tfidf = vectorizer.fit_transform(documents)
    scores = np.asarray(tfidf.mean(axis=0)).ravel()
    phrases = vectorizer.get_feature_names_out()

    ranked = sorted(
        zip(phrases, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]
