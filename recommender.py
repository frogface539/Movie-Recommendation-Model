import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("Notebooks/movies.csv")
ratings = pd.read_csv("Notebooks/ratings.csv", usecols=["movieId", "rating"], nrows=500_000)

movie_genre_features = pd.read_pickle("model/movie_genre_features.pkl")

genre_vectors = movie_genre_features.drop(['movieId', 'title'], axis=1)

avg_ratings = ratings.groupby("movieId")["rating"].mean().reset_index()
avg_ratings.columns = ["movieId", "avg_rating"]

def recommend_similar_movies(title, top_n=10):
    matches = movie_genre_features[movie_genre_features['title'].str.lower() == title.lower()]
    if matches.empty:
        return None
    idx = matches.index[0]
    similarities = cosine_similarity([genre_vectors.iloc[idx]], genre_vectors)[0]
    similar_indices = similarities.argsort()[::-1][1:top_n + 1]
    similar_movies = movie_genre_features.iloc[similar_indices][['movieId', 'title']]
    merged = similar_movies.merge(movies[['movieId', 'genres']], on='movieId', how='left')
    merged = merged.merge(avg_ratings, on='movieId', how='left')
    return merged[['title', 'genres', 'avg_rating']].reset_index(drop=True)

def get_all_titles():
    return sorted(movie_genre_features['title'].unique())
