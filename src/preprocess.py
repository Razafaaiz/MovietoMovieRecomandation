import pandas as pd

def load_datasets(data_path="../data/"):
    """
    Load CSV datasets: movies, ratings, tags, links
    """
    movies = pd.read_csv(f"{data_path}/movies.csv")
    ratings = pd.read_csv(f"{data_path}/ratings.csv")
    tags = pd.read_csv(f"{data_path}/tags.csv")
    links = pd.read_csv(f"{data_path}/links.csv")
    return movies, ratings, tags, links

