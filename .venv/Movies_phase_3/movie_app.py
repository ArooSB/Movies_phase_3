class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.get_movies()
        if not movies:
            print("No movies found.")
        else:
            print(f"{len(movies)} movies in total")
            for movie, details in movies.items():
                year = details.get("year")
                rating = details.get("rating")
                print(f"{movie}: {year} - Rating: {rating}")

    def _command_add_movie(self):
        title = input("Enter the movie title: ").strip()
        year = input("Enter the release year: ").strip()
        try:
            rating = float(input("Enter the movie rating: ").strip())
        except ValueError:
            print("Invalid rating value. Please enter a number.")
            return
        self._storage.add_movie(title, year, rating)
        print(f"Added '{title}' to the movie collection.")

    def _command_delete_movie(self):
        title = input("Enter the movie title to delete: ").strip()
        self._storage.delete_movie(title)
        print(f"Deleted '{title}' from the movie collection.")

    def _command_search_movie(self):
        query = input("Enter movie name to search: ").strip().lower()
        movies = self._storage.get_movies()
        matching_movies = {
            title: details for title, details in movies.items() if query in title.lower()
        }
        if not matching_movies:
            print("No matching movies found.")
        else:
            for title, details in matching_movies.items():
                print(f"{title}: Year {details['year']}, Rating {details['rating']}")

    def _command_update_movie(self):
        title = input("Enter the movie title to update: ").strip()
        try:
            new_rating = float(input("Enter the new rating: ").strip())
        except ValueError:
            print("Invalid rating value. Please enter a number.")
            return
        self._storage.update_movie(title, new_rating)
        print(f"The rating for '{title}' has been updated to {new_rating}.")

    def _command_average_rating(self):
        movies = self._storage.get_movies()
        if not movies:
            print("No movies available to calculate average rating.")
            return
        total_rating = sum(details["rating"] for details in movies.values())
        average_rating = total_rating / len(movies)
        print(f"The average rating: {average_rating:.2f}")

    def _command_median_rating(self):
        movies = self._storage.get_movies()
        if not movies:
            print("No movies available to calculate median rating.")
            return
        sorted_ratings = sorted(details["rating"] for details in movies.values())
        num_ratings = len(sorted_ratings)
        if num_ratings % 2 == 0:
            mid_index = num_ratings // 2
            median_rating = (sorted_ratings[mid_index - 1] + sorted_ratings[mid_index]) / 2
        else:
            mid_index = num_ratings // 2
            median_rating = sorted_ratings[mid_index]
        print(f"The median rating is: {median_rating:.2f}")

    def _command_best_rating(self):
        movies = self._storage.get_movies()
        if not movies:
            print("No movies available to determine best rating.")
            return
        max_rating = max(details["rating"] for details in movies.values())
        best_movies = [
            movie for movie, details in movies.items() if details["rating"] == max_rating
        ]
        print(f"The best movie(s): {best_movies}, with rating {max_rating}")

    def _command_worst_rating(self):
        movies = self._storage.get_movies()
        if not movies:
            print("No movies available to determine worst rating.")
            return
        min_rating = min(details["rating"] for details in movies.values())
        worst_movies = [
            movie for movie, details in movies.items() if details["rating"] == min_rating
        ]
        print(f"The worst movie(s): {worst_movies}, with rating {min_rating}")

    def _command_random_movie(self):
        import random
        movies = self._storage.get_movies()
        if not movies:
            print("No movies available to pick a random movie.")
            return
        movie_name, details = random.choice(list(movies.items()))
        year = details.get("year")
        rating = details.get("rating")
        print(f"Random movie: {movie_name} - Year: {year} - Rating: {rating:.1f}")

    def run(self):
        while True:
            print("Select options:")
            print("0. Exit")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Search movie")
            print("5. Update movie")
            print("6. Average rating")
            print("7. Median rating")
            print("8. Best rating")
            print("9. Worst rating")
            print("10. Random movie")
            action = input("Enter choice (0-10): ").strip()

            if action == "0":
                print("Bye!")
                break
            elif action == "1":
                self._command_list_movies()
            elif action == "2":
                self._command_add_movie()
            elif action == "3":
                self._command_delete_movie()
            elif action == "4":
                self._command_search_movie()
            elif action == "5":
                self._command_update_movie()
            elif action == "6":
                self._command_average_rating()
            elif action == "7":
                self._command_median_rating()
            elif action == "8":
                self._command_best_rating()
            elif action == "9":
                self._command_worst_rating()
            elif action == "10":
                self._command_random_movie()
            else:
                print("Invalid choice. Please enter a number from 0 to 10.")
