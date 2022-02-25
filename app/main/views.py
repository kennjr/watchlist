from flask import render_template, url_for
# the fun we get from the import abv. (render_template()) takes in the name of html file asan arg and loads the
# file after searching for it in the app/templates/ dir
from werkzeug.utils import redirect

from app import app
# The import abv. is an import of the app instance from the app dir

# from request import api_key
from app import request
from flask import request as req

from app.main import main
from app.model import reviews
# import model.reviews
from app.main.forms import ReviewForm
Review = reviews.Review


# Views
@main.route('/')
# The line abv. is a route decorator that we use to pass the route the fun below it is for
def index():
    """
    View root page function that returns the index page and its data
    """
    search_movie = req.args.get('search_str')
    if search_movie:
        return redirect(url_for('main.search', search_str=search_movie))
    else:
        return render_template('index.html', message=request.api_key)


@main.route("/movies/popular")
def popular_movies():
    popular_movies = request.get_movies("popular")
    return render_template("movies.html", title="Popular movies", movies_list=popular_movies)


@main.route("/movie/<movie_id>")
def movie(movie_id):
    """
    View movie page function that returns the movie details page and its data
    """
    movie = request.get_movie(movie_id)
    reviews = Review.get_reviews(movie.movie_id)
    return render_template("movie.html", movie=movie, id=movie_id, title=movie.title, reviews=reviews)


@main.route("/search/<search_str>")
def search(search_str):
    search_str_list = search_str.split(" ")
    search_str_format = "+".join(search_str_list)
    searched_movies = request.search_movie(search_str_format)
    title = f'search results for {search_str}'
    return render_template("search.html", movies=searched_movies, title=title)


@main.route('/movie/review/new/<int:movie_id>', methods=['GET', 'POST'])
def new_review(movie_id):
    form = ReviewForm()
    movie = request.get_movie(movie_id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.movie_id, title, movie.poster, review)
        new_review.save_review()
        return redirect(url_for('main.movie', movie_id=movie.movie_id))

    title = f'{movie.title} review'
    return render_template('new_review.html', title=title, review_form=form, movie=movie)
