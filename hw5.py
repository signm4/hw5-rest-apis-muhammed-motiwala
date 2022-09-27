import os
import requests
from dotenv import load_dotenv, find_dotenv

def get_top_10_weekly_trending_movies ():

    load_dotenv()
    api_key = os.getenv('TMDB_API_KEY')

    
    TMDB_TRENDING_MOVIE_API_REQUEST = 'https://api.themoviedb.org/3'
    response =  requests.get(
        f"{TMDB_TRENDING_MOVIE_API_REQUEST}/trending/movie/week",
        params={'api_key' : api_key }
        )

    json_data = response.json()

    weekly_trending_movie_obj = json_data
    weekly_trending_movie_list = weekly_trending_movie_obj['results']

    for i in range(10):
        print(weekly_trending_movie_list[i]["title"])



get_top_10_weekly_trending_movies()