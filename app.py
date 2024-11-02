from flask import Flask, render_template, request
from src.data_loader import load_data
from src.recommender import Recommender

app = Flask(__name__)

# Load data and initialize recommender
movies, songs, news_articles = load_data()
recommender = Recommender(movies, songs, news_articles)

@app.route('/', methods=['GET', 'POST'])
def index():
    movie_recommendations = []
    song_recommendations = []
    news_recommendations = []

    # Get the full lists to display
    movie_list = movies['title'].tolist()
    song_list = songs['title'].tolist()
    news_list = news_articles['title'].tolist()

    if request.method == 'POST':
        if request.form.get('movie'):
            movie_title = request.form['movie']
            movie_recommendations = recommender.recommend_movies(movie_title)

        if request.form.get('song'):
            song_title = request.form['song']
            song_recommendations = recommender.recommend_songs(song_title)

        if request.form.get('news'):
            article_title = request.form['news']
            news_recommendations = recommender.recommend_news(article_title)

    return render_template('index.html',
                           movie_recommendations=movie_recommendations,
                           song_recommendations=song_recommendations,
                           news_recommendations=news_recommendations,
                           movie_list=movie_list,
                           song_list=song_list,
                           news_list=news_list)

if __name__ == '__main__':
    app.run(debug=True)
