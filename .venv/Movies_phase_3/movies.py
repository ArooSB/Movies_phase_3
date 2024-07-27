import random
import difflib
import movie_storage
import omdb_api
import requests

API_KEY = "b489c489"


def get_country_flag(country):
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}?fullText=true")
        response.raise_for_status()
        country_info = response.json()
        return country_info[0]['flags']['png']  # URL to the flag image
    except requests.RequestException as e:
        print(f"Error fetching flag for country {country}: {e}")
        return None


def list_movies():
    movies = movie_storage.get_movies()
    print(len(movies), "movies in total")
    for movie, details in movies.items():
        year = details.get("year")
        rating = details.get("rating")
        poster = details.get("poster")
        country = details.get("country")
        print(f"{movie}: {year} - Rating: {rating} - Poster: {poster} - Country: {country}")


def add_movie(title):
    movies = movie_storage.get_movies()
    if title in movies:
        print("Movie already in the list")
        return
    else:
        details = omdb_api.fetch_movie_details(API_KEY, title)
        if details:
            year = details.get("Year")
            rating = float(details.get("imdbRating", 0))
            poster = details.get("Poster")
            imdb_id = details.get("imdbID")
            country = details.get("Country")
            movie_storage.add_movie(title, year, rating, poster, imdb_id, country)
            print(f"Added '{title}' to the movie collection.")
        else:
            print("Movie not found or there was an error accessing the OMDb API.")


def delete_movie(title):
    movie_storage.delete_movie(title)
    print(f"Deleted '{title}' from the movie collection.")


def search_movie(query):
    movies = movie_storage.get_movies()
    movie_titles = [movie.lower() for movie in movies.keys()]
    matching_titles = difflib.get_close_matches(query, movie_titles, n=10, cutoff=0.1)

    matching_movies = [
        (movie, details["rating"])
        for movie, details in movies.items()
        if movie.lower() in matching_titles
    ]
    for movie, rating in matching_movies:
        print(movie + ",", rating)


def update_movie(title, new_rating):
    if title not in movie_storage.get_movies():
        print("Movie not found.")
    else:
        movie_storage.update_movie(title, float(new_rating))
        print(f"The rating for '{title}' has been updated to {new_rating}.")


def average_movie_rating():
    movies = movie_storage.get_movies()
    total_rating = sum(details["rating"] for details in movies.values())
    average_rating = total_rating / len(movies)
    print(f"The average rating: {average_rating:.2f}")
    return average_rating


def calculate_median_rating():
    movies = movie_storage.get_movies()
    sorted_ratings = sorted(details["rating"] for details in movies.values())
    num_ratings = len(sorted_ratings)
    if num_ratings % 2 == 0:
        mid_index = num_ratings // 2
        median_rating = (sorted_ratings[mid_index - 1] + sorted_ratings[mid_index]) / 2
    else:
        mid_index = num_ratings // 2
        median_rating = sorted_ratings[mid_index]
    print(f"The median rating is: {median_rating:.2f}")
    return median_rating


def best_rating():
    movies = movie_storage.get_movies()
    max_rating = max(details["rating"] for details in movies.values())
    best_movies = [
        movie for movie, details in movies.items() if details["rating"] == max_rating
    ]
    print(f"The best movie(s): {best_movies}, with rating {max_rating}")
    return best_movies, max_rating


def worst_rating():
    movies = movie_storage.get_movies()
    min_rating = min(details["rating"] for details in movies.values())
    worst_movies = [
        movie for movie, details in movies.items() if details["rating"] == min_rating
    ]
    print(f"The worst movie(s): {worst_movies}, with rating {min_rating}")
    return worst_movies, min_rating


def random_movie():
    movies = movie_storage.get_movies()
    movie_name, details = random.choice(list(movies.items()))
    year = details.get("year")
    rating = details.get("rating")
    poster = details.get("poster")
    print(f"Random movie: {movie_name} - Year: {year} - Rating: {rating:.1f} - Poster: {poster}")
