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
## ⚙️ Installation & Setup

1️⃣ Clone Repository

git clone https://github.com/YourUsername/HybridRecommendationSystem.git
cd HybridRecommendationSystem

2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate      # Windows  

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run Streamlit App

streamlit run app/app.py

## 🧠 How It Works

📌 Workflow

📝 Load movies.csv (title + genres)

🔡 Convert into combined text → "Title + Genres"

🧠 Generate embeddings with Sentence-BERT

⚡ Store & search vectors with FAISS

🎬 Display Top-N Recommendations in Streamlit

## 🛠️ Tech Stack

🐍 Python 3.11

🎨 Streamlit – Frontend UI

🧠 Sentence-BERT – NLP embeddings

⚡ FAISS – Similarity Search Engine

📊 Pandas & NumPy – Data Processing

## 🌐 Deployment

Deploy easily on Streamlit Cloud:

Push your repo to GitHub

Go to Streamlit Cloud

Connect GitHub → Select repo → Deploy 🚀

Get live app at: https://movietomovierecomandation.streamlit.app/

## 🎯 Why This Project?

✔️ Real-world Recommendation System project

✔️ Showcases Modern NLP & Vector Search

✔️ Clean & Deployable – ready for GitHub & Streamlit Cloud

✔️ Excellent addition to Data Science / ML portfolio

<div align="center">
✨ Movie to Movie Recommendations | 🚀 Built with Streamlit + SBERT + FAISS | 2025 ✨
</div> 
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








