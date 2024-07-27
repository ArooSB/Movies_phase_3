import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, filepath):
        self.filepath = filepath

    def _read_data(self):
        """Reads data from the CSV file and returns it as a dictionary."""
        movies = {}
        try:
            with open(self.filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    title = row['title']
                    movies[title] = {
                        'rating': float(row['rating']),
                        'year': int(row['year']),
                        'poster': row.get('poster'),
                        'imdb_id': row.get('imdb_id'),
                        'country': row.get('country')
                    }
        except FileNotFoundError:
            pass  # If the file doesn't exist, return an empty dictionary
        return movies

    def _write_data(self, movies):
        """Writes the movie data to the CSV file."""
        fieldnames = ['title', 'rating', 'year', 'poster', 'imdb_id', 'country']
        with open(self.filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for title, details in movies.items():
                row = {'title': title}
                row.update(details)
                writer.writerow(row)

    def list_movies(self):
        """Returns a dictionary of all movies."""
        return self._read_data()

    def add_movie(self, title, year, rating, poster=None, imdb_id=None, country=None):
        """Adds a movie to the collection."""
        movies = self._read_data()
        movies[title] = {
            "year": year,
            "rating": rating,
            "poster": poster,
            "imdb_id": imdb_id,
            "country": country
        }
        self._write_data(movies)

    def delete_movie(self, title):
        """Deletes a movie from the collection by title."""
        movies = self._read_data()
        if title in movies:
            del movies[title]
            self._write_data(movies)

    def update_movie(self, title, rating):
        """Updates the rating of a movie."""
        movies = self._read_data()
        if title in movies:
            movies[title]["rating"] = rating
            self._write_data(movies)
