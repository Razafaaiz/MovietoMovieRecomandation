import numpy as np

def recommend_hybrid(user_idx, cf_model, embeddings, faiss_index, alpha=0.5, top_k=10):
    """
    Hybrid recommendation: alpha * CF + (1-alpha) * content-based
    """
    # 1. CF predictions
    num_movies = embeddings.shape[0]
    movie_indices = np.arange(num_movies)
    user_array = np.full_like(movie_indices, user_idx)
    cf_scores = cf_model.predict([user_array, movie_indices], verbose=0).flatten()

    # 2. Content-based similarity
    cb_scores = np.zeros(num_movies)
    for m_idx in movie_indices:
        vector = embeddings[m_idx].reshape(1, -1).astype('float32')
        D, I = faiss_index.search(vector, num_movies)
        cb_scores[I[0]] += 1 / (1 + D[0])
    if cb_scores.sum() > 0:
        cb_scores /= cb_scores.max()

    # 3. Hybrid score
    hybrid_scores = alpha * cf_scores + (1 - alpha) * cb_scores
    top_indices = hybrid_scores.argsort()[-top_k:][::-1]
    return top_indices

