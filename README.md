<div align="center">

# 🎬 Hybrid Movie Recommendation System 🍿  

[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)](https://streamlit.io)  
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)  
[![FAISS](https://img.shields.io/badge/Search-FAISS-green)](https://github.com/facebookresearch/faiss)  
[![Sentence-BERT](https://img.shields.io/badge/Embeddings-SBERT-orange)](https://www.sbert.net/)  

✨ A real-world **Movie Recommender System** powered by **Streamlit, Sentence-BERT, and FAISS**.  
Type a **movie title, keyword, or genre**, and get instant **personalized movie suggestions**.  

</div>  

---

## 🚀 Features  

- 🎨 **Interactive Web App** – Built with Streamlit  
- 🧠 **Sentence-BERT Embeddings** – Semantic understanding of movies  
- ⚡ **FAISS Similarity Search** – Super-fast vector matching  
- 📂 **Lightweight Dataset** – Only `movies.csv` (no heavy files)  
- 🔍 **Search by Title, Keyword, or Genre**  
- 🌐 **Deployable** – Streamlit Cloud / HuggingFace Spaces  

---

## 🏗️ Project Structure  

```plaintext
HybridRecommendationSystem/
│
├── app/                  # Streamlit app
│   └── app.py            # Main entry point
│
├── src/                  
│   ├── content_based.py  # Embedding + Recommendation logic
│   └── utils.py          # Helper functions
│
├── data/                 
│   └── movies.csv        # Movie dataset (title + genres only)
│
├── train.py              # Script for building embeddings
├── requirements.txt      # Dependencies
├── .gitignore            # Ignore unnecessary files
└── README.md             # Documentation
