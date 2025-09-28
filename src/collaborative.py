'''import tensorflow as tf
from tensorflow.keras import layers, Model
import numpy as np

def build_cf_model(num_users, num_movies, embedding_size=64):
    """
    Neural Collaborative Filtering model
    """
    user_input = layers.Input(shape=(1,))
    user_emb = layers.Embedding(num_users, embedding_size)(user_input)
    user_vec = layers.Flatten()(user_emb)

    movie_input = layers.Input(shape=(1,))
    movie_emb = layers.Embedding(num_movies, embedding_size)(movie_input)
    movie_vec = layers.Flatten()(movie_emb)

    x = layers.Concatenate()([user_vec, movie_vec])
    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dense(64, activation='relu')(x)
    output = layers.Dense(1, activation='sigmoid')(x)

    model = Model([user_input, movie_input], output)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
'''
