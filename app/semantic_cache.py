import numpy as np

cache = []

SIMILARITY_THRESHOLD = 0.90


def cosine_similarity(vector_a, vector_b):
    a = np.array(vector_a)
    b = np.array(vector_b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def find_similar_answer(query_embedding):

    best_match = None
    best_score = 0

    for item in cache:

        score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        if score > best_score:
            best_score = score
            best_match = item

    if best_score >= SIMILARITY_THRESHOLD:
        return best_match, best_score

    return None, best_score


def save_to_cache(query, embedding, answer):

    cache.append({
        "query": query,
        "embedding": embedding,
        "answer": answer
    })
