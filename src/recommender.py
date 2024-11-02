import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, movies, songs, news_articles):
        self.movies = movies
        self.songs = songs
        self.news_articles = news_articles

    def recommend_movies(self, movie_title):
        movie_idx = self.movies[self.movies['title'] == movie_title].index[0]
        cosine_sim = cosine_similarity(self.movies[['genre']].values)
        similar_movies = list(enumerate(cosine_sim[movie_idx]))
        similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
        return [self.movies.iloc[i[0]]['title'] for i in similar_movies[1:6]]

    def recommend_songs(self, song_title):
        song_idx = self.songs[self.songs['title'] == song_title].index[0]
        cosine_sim = cosine_similarity(self.songs[['genre']].values)
        similar_songs = list(enumerate(cosine_sim[song_idx]))
        similar_songs = sorted(similar_songs, key=lambda x: x[1], reverse=True)
        return [self.songs.iloc[i[0]]['title'] for i in similar_songs[1:6]]

    def recommend_news(self, article_title):
        article_idx = self.news_articles[self.news_articles['title'] == article_title].index[0]
        cosine_sim = cosine_similarity(self.news_articles[['category']].values)
        similar_articles = list(enumerate(cosine_sim[article_idx]))
        similar_articles = sorted(similar_articles, key=lambda x: x[1], reverse=True)
        return [self.news_articles.iloc[i[0]]['title'] for i in similar_articles[1:6]]
