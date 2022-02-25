import json
import urllib.request
from app import app, models

# from models import Movie



# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIES_DB_BASE_URL']


def process_results(movie_results_list):
    """
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_results_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    """
    movie_results = []
    for movie_item in movie_results_list:
        movie_id = movie_item['id']
        title = movie_item.get('original_title')
        overview = movie_item.get("overview")
        poster = movie_item.get("poster_path")
        vote_avg = movie_item.get("vote_average")
        vote_count = movie_item.get("vote_count")

        if poster:
            movie_obj = models.Movie(movie_id, title, overview, poster, vote_avg, vote_count)
            movie_results.append(movie_obj)

    return movie_results


def get_movies(category):
    # the line below will format url and replace the curly braces with the category and the api_key resp.
    get_movies_url = base_url.format(category, api_key)

    # we're using the with as our context manager to send a request using urllib.request.urlopen()
    with urllib.request.urlopen(get_movies_url) as url:
        #  we use the url.read() fun to read the response and store it in the var get_movies_data
        get_movies_data = url.read()

        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response["results"]:
            movie_results_list = get_movies_response["results"]
            movie_results = process_results(movie_results_list)

    return movie_results


def get_movie(movie_id):
    get_movie_details_url = base_url.format(movie_id, api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_obj = None
        if movie_details_response:
            the_id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get("overview")
            poster = movie_details_response.get("poster_path")
            vote_avg = movie_details_response.get("vote_average")
            vote_count = movie_details_response.get("vote_count")

            movie_obj = models.Movie(the_id, title, overview, poster, vote_avg, vote_count)

        return movie_obj


def search_movie(search_str):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key, search_str)
    # search_movie_url = "https://api.themoviedb.org/3/search/movie?api_key={}&query={}".format(api_key, search_str)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_results = None
        print(search_results)
        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']

            search_results = process_results(search_movie_list)

    return search_results
