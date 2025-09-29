import pandas as pd
import os

def load_movies(path="data/movies.csv"):
    """
    Load only the movies dataset.
    Args:
        path (str): Path to movies.csv
    Returns:
        pd.DataFrame: Movies dataframe with movieId, title, and genres
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ movies.csv not found at {path}")
    
    movies = pd.read_csv(path)
    return movies


def save_embeddings(embeddings, path="models/movie_embeddings.npy"):
    """
    Save movie embeddings to a .npy file.
    """
    import numpy as np
    np.save(path, embeddings)


def load_embeddings(path="models/movie_embeddings.npy"):
    """
    Load movie embeddings from a .npy file.
    """
    import numpy as np
    return np.load(path)


def save_faiss_index(faiss_index, path="models/faiss.index"):
    """
    Save FAISS index to file.
    """
    import faiss
    faiss.write_index(faiss_index, path)


def load_faiss_index(path="models/faiss.index"):
    """
    Load FAISS index from file.
    """
    import faiss
    return faiss.read_index(path)

