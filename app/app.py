import sys
import os
import streamlit as st
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from src.content_based import recommend_movies_by_typing

# -----------------------------
# Add project root to sys.path
# -----------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="🎬 Movie-to-Movie Recommendation System",
    page_icon="🎥",
    layout="wide",
)

# -----------------------------
# Load models and data
# -----------------------------
@st.cache_resource
def load_models():
    with open("models/movies.pkl", "rb") as f:
        movies = pickle.load(f)
    embeddings = np.load("models/movie_embeddings.npy")
    faiss_index = faiss.read_index("models/faiss.index")
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    return movies, embeddings, faiss_index, embedder

movies, embeddings, faiss_index, embedder = load_models()

# -----------------------------
# App UI
# -----------------------------
st.title("🎬 Movie-to-Movie Recommendation System")
st.markdown(
    """
    Welcome! Type a movie title, keyword, or genre and click **Recommend**.
    The system will show you top-rated movies most similar to your query.
    """
)

query = st.text_input("Search for a movie or keyword:")

if st.button("**Recommend**"):
    if query.strip() == "":
        st.warning("Please type something to get recommendations!")
    else:
        # Get recommendations
        recs = recommend_movies_by_typing(query, movies, embeddings, faiss_index, embedder, top_n=10)

        # Display only the existing columns: title, genres, rating
        recs_display = recs[['title', 'genres', 'rating']].sort_values(by='rating', ascending=False)

        st.subheader("🌟 Top Recommendations")
        for idx, row in recs_display.iterrows():
            st.markdown(
                f"**{row['title']}**  \nGenres: {row['genres']}  \nRating: {row['rating']:.1f}"
            )

        st.markdown("---")
        st.info("Top movies are sorted from highest rating to lowest for your convenience rated from 5 to 1.")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <hr style="border:1px solid #eee">
    <p style='text-align: center; font-size:12px;'>Movie-to-Movie Recommendation System | Built with Streamlit, FAISS, Sentence-BERT | 2025</p>
    """, unsafe_allow_html=True
)









