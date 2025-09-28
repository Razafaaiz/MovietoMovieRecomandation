import numpy as np
import faiss

def save_embeddings(embeddings, file_path):
    np.save(file_path, embeddings)

def load_embeddings(file_path):
    return np.load(file_path)

def save_faiss_index(faiss_index, file_path):
    faiss.write_index(faiss_index, file_path)

def load_faiss_index(file_path):
    return faiss.read_index(file_path)

