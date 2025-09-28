import os
import pickle
import pandas as pd
from src.content_based import build_embeddings
from src.utils import save_embeddings, save_faiss_index

# -----------------------------
# Helper function to load datasets
# -----------------------------
def load_datasets(data_dir="data"):
    """
    Load movies, ratings, tags, and links datasets from given folder.
    
    Returns:
        movies, ratings, tags, links (pd.DataFrame)
    """
    movies = pd.read_csv(os.path.join(data_dir, "movies.csv"))
    ratings = pd.read_csv(os.path.join(data_dir, "ratings.csv"))
    tags = pd.read_csv(os.path.join(data_dir, "tags.csv"))
    links = pd.read_csv(os.path.join(data_dir, "links.csv"))
    return movies, ratings, tags, links

# -----------------------------
# Load datasets
# -----------------------------
movies, ratings, tags, links = load_datasets("data")

# -----------------------------
# Merge average ratings into movies
# -----------------------------
avg_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()
movies = movies.merge(avg_ratings, on='movieId', how='left')

# -----------------------------
# Build embeddings + FAISS index (CPU only)
# -----------------------------
embeddings, faiss_index, embedder = build_embeddings(movies)

# -----------------------------
# Create models folder
# -----------------------------
os.makedirs("models", exist_ok=True)

# -----------------------------
# Save embeddings and FAISS index
# -----------------------------
save_embeddings(embeddings, "models/movie_embeddings.npy")
save_faiss_index(faiss_index, "models/faiss.index")

# -----------------------------
# Save processed movies DataFrame
# -----------------------------
with open("models/movies.pkl", "wb") as f:
    pickle.dump(movies, f)

print("✅ Embeddings, FAISS index, and movies.pkl saved to models/")


