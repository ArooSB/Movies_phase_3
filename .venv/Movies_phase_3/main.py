from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

def main():
    # Example using JSON storage
    json_storage = StorageJson('movies.json')
    movie_app_json = MovieApp(json_storage)
    movie_app_json.run()

    # Example using CSV storage
    csv_storage = StorageCsv('movies.csv')
    movie_app_csv = MovieApp(csv_storage)
    movie_app_csv.run()

if __name__ == "__main__":
    main()
