import pandas as pd

def load_data():
    movies = pd.read_csv('data/movies.csv')
    songs = pd.read_csv('data/songs.csv')
    news_articles = pd.read_csv('data/news_articles.csv')
    return movies, songs, news_articles
