import json
from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, filename='movies.json'):
        self.filename = filename

    def get_movies(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_movies(self, movies):
        with open(self.filename, 'w') as file:
            json.dump(movies, file, indent=4)

    def add_movie(self, title, year, rating):
        movies = self.get_movies()
        movies[title] = {"year": year, "rating": rating}
        self.save_movies(movies)

    def delete_movie(self, title):
        movies = self.get_movies()
        if title in movies:
            del movies[title]
            self.save_movies(movies)

    def update_movie(self, title, rating):
        movies = self.get_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self.save_movies(movies)
