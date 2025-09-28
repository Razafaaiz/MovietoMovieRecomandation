from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd
import os

def build_embeddings(movies, model_name='all-MiniLM-L6-v2'):
    """
    Build Sentence-BERT embeddings for movies and FAISS index (CPU only)
    """
    # Force CPU
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    
    movies['text'] = movies['title'] + " " + movies['genres']
    embedder = SentenceTransformer(model_name)
    
    embeddings = embedder.encode(movies['text'].tolist(), show_progress_bar=True)
    
    embedding_dim = embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(embedding_dim)
    faiss_index.add(embeddings.astype('float32'))
    
    return embeddings, faiss_index, embedder


def recommend_movies_by_typing(query, movies, embeddings, faiss_index, embedder, top_n=10):
    """
    Recommend movies based on user typing a query, sorted by highest rating.

    Args:
        query (str): User input (movie name, keywords, etc.)
        movies (pd.DataFrame): DataFrame with movie metadata, must include 'rating'
        embeddings (np.ndarray): Precomputed movie embeddings
        faiss_index (faiss.Index): FAISS index built from embeddings
        embedder (SentenceTransformer): The same Sentence-BERT model
        top_n (int): Number of recommendations to return

    Returns:
        pd.DataFrame: Recommended movies with only title, genres, and rating
    """
    # Encode query
    query_embedding = embedder.encode([query])

    # Search in FAISS index
    distances, indices = faiss_index.search(
        np.array(query_embedding).astype('float32'), top_n
    )

    # Collect results
    results = movies.iloc[indices[0]].copy()

    # Ensure 'rating' column exists
    if 'rating' not in results.columns:
        raise ValueError("The movies DataFrame must have a 'rating' column.")

    # Sort by rating descending
    results_sorted = results.sort_values(by='rating', ascending=False)

    # Return only title, genres, and rating
    return results_sorted[['title', 'genres', 'rating']].reset_index(drop=True)






