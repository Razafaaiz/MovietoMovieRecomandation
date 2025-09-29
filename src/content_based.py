from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd
import os


def build_embeddings(movies, model_name='all-MiniLM-L6-v2'):
    """
    Build Sentence-BERT embeddings for movies and FAISS index (CPU only).
    """
    # Force CPU
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    
    # Combine title + genres for embedding
    movies['text'] = movies['title'] + " " + movies['genres']
    embedder = SentenceTransformer(model_name)
    
    embeddings = embedder.encode(movies['text'].tolist(), show_progress_bar=True)
    
    embedding_dim = embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(embedding_dim)
    faiss_index.add(embeddings.astype('float32'))
    
    return embeddings, faiss_index, embedder


def recommend_movies_by_typing(query, movies, embeddings, faiss_index, embedder, top_n=10):
    """
    Recommend movies based on user typing a query.
    Only returns title and genres (no rating required).
    """
    # Encode query
    query_embedding = embedder.encode([query])

    # Search in FAISS index
    distances, indices = faiss_index.search(
        np.array(query_embedding).astype('float32'), top_n
    )

    # Collect results
    results = movies.iloc[indices[0]].copy()

    # Return only title + genres
    return results[['title', 'genres']].reset_index(drop=True)







