import os
import requests
from dotenv import load_dotenv

def get_top_10_weekly_trending_movies ():

    #using dot env file and pulling key from .env file
    load_dotenv()
    api_key = os.getenv('TMDB_API_KEY')

    #made base URL, requests.get will pull the trending movies, also need api key to access
    TMDB_TRENDING_MOVIE_API_REQUEST = 'https://api.themoviedb.org/3'
    response =  requests.get(
        f"{TMDB_TRENDING_MOVIE_API_REQUEST}/trending/movie/week",
        params={'api_key' : api_key }
        )

    #Fill everything into json_data
    json_data = response.json()
    # fill data into weekly obj
    weekly_trending_movie_obj = json_data
    #just pulling the list of movies
    weekly_trending_movie_list = weekly_trending_movie_obj['results']
    #only needing top 10 movies so for loop does that
    for i in range(10):
        print(weekly_trending_movie_list[i]["title"])


#run the file
get_top_10_weekly_trending_movies()