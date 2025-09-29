'''import streamlit as st
import sys
import os
import pandas as pd

# --- Fix imports ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

from content_based import build_embeddings, recommend_movies_by_typing
from utils import load_movies   # we'll define this in utils.py

# --- Page Config ---
st.set_page_config(
    page_title="🎬 Movie to Movie Recommendations",
    page_icon="🍿",
    layout="centered"
)

# --- Title ---
st.title("🎬 Movie to Movie Recommendations")
st.write(  """
    Welcome! Type a movie title, keyword, or genre and click **Recommend**.
    The system will show you top-rated movies most similar to your query.
    """)
st.sidebar.info("🚀 Type a movie title or genre and click Recommend! Made by: **Faiz Raza**")

# --- Load Movies Dataset ---
@st.cache_resource
def load_data():
    movies = load_movies("data/movies.csv")  # only movies.csv needed
    embeddings, faiss_index, embedder = build_embeddings(movies)
    return movies, embeddings, faiss_index, embedder


movies, embeddings, faiss_index, embedder = load_data()


# --- User Input ---
query = st.text_input("🔍 Search for a movie or genre:")

if st.button("**Recommend**"):
    if query.strip() == "":
        st.warning("⚠️ Please type something to search!")
    else:
        recs = recommend_movies_by_typing(query, movies, embeddings, faiss_index, embedder, top_n=10)

        if recs.empty:
            st.error("❌ No recommendations found.")
        else:
            st.success(f"🍿 Top {len(recs)} recommendations for: **{query}**")
            st.dataframe(recs[['title', 'genres']], use_container_width=True)


# Footer
# -----------------------------
st.markdown(
    """
    <hr style="border:1px solid #eee">
    <p style='text-align: center; font-size:12px;'>Movie to Movie Recommendations | 🚀 Built with Streamlit, FAISS, Sentence-BERT | 2025</p>
    """, unsafe_allow_html=True
)'''
import streamlit as st
import sys
import os
import pandas as pd

# --- Fix imports ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

from content_based import build_embeddings, recommend_movies_by_typing
from utils import load_movies

# --- Page Config ---
st.set_page_config(
    page_title="🎬 Movie-to-Movie Recommender",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar ---
st.sidebar.header("🔧 Project Info")
st.sidebar.markdown("""
**Movie to Movie Recommendations**  

**Purpose:**  
- Suggest movies similar to a given movie or keyword  
- Helps users discover new content based on similarity
- Returns top 10 closest movies to your query  
  
""")
st.sidebar.info("🚀 Type a movie title or genre and click Recommend!")



# --- Main Title ---
st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B;'>🎬 Movie-to-Movie Recommender</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: grey; font-size:16px;'>Find movies similar to your favorite movies or genres</p>",
    unsafe_allow_html=True
)

# --- Load Movies Dataset ---
@st.cache_resource
def load_data():
    movies = load_movies("data/movies.csv")
    embeddings, faiss_index, embedder = build_embeddings(movies)
    return movies, embeddings, faiss_index, embedder

movies, embeddings, faiss_index, embedder = load_data()

# --- User Input ---
st.markdown("### 🔍 Search for a movie or genre:")
query = st.text_input("", placeholder="Type a movie title, keyword, or genre here...")

# --- Recommend Button ---
if st.button("🍿 Recommend"):
    if query.strip() == "":
        st.warning("⚠️ Please type something to search!")
    else:
        recs = recommend_movies_by_typing(query, movies, embeddings, faiss_index, embedder, top_n=10)

        if recs.empty:
            st.error("❌ No recommendations found.")
        else:
            st.success(f"🍿 Top {len(recs)} recommendations for: **{query}**")

            # --- Display as cards ---
            for idx, row in recs.iterrows():
                st.markdown(
                    f"""
                    <div style='padding:10px; margin:5px; background-color:#FFF2E7; border-radius:10px; box-shadow: 1px 1px 5px #ccc'>
                        <h4 style='margin:0; color:#FF4B4B;'>{row['title']}</h4>
                        <p style='margin:0; color:#555;'>{row['genres']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# --- Footer ---
st.markdown(
    """
    <hr style="border:1px solid #eee">
    <p style='text-align: center; font-size:12px; color: grey;'>
    Movie-to-Movie Recommendations | 🚀 Built with Streamlit, FAISS, Sentence-BERT | 2025
    </p>
    """,
    unsafe_allow_html=True
)










