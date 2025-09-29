import sys
import os

# Add src folder to Python path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

# Now you can import from src
from content_based import build_embeddings
from utils import save_embeddings, save_faiss_index, load_movies


# --- Load Movies Dataset ---
movies = load_movies("data/movies.csv")
print(f"✅ Loaded {len(movies)} movies.")

# --- Build Embeddings + FAISS Index ---
print("⏳ Building embeddings and FAISS index ... this may take a few seconds")
embeddings, faiss_index, embedder = build_embeddings(movies)
print("✅ Embeddings and FAISS index built successfully!")

# --- Create models folder if not exists ---
os.makedirs("models", exist_ok=True)

# --- Save embeddings and FAISS index ---
save_embeddings(embeddings, "models/movie_embeddings.npy")
save_faiss_index(faiss_index, "models/faiss.index")
print("✅ Embeddings and FAISS index saved to models/")



