import mysql.connector
from api.movie_class import Movie

class MovieListDB:
    def __init__(self):
        self._movies = self._load_movies()

    def _load_movies(self):
        movies = []
        try:
            with get_connection(self) as db:
                cursor = db.cursor()
                cursor.execute("SELECT * FROM movie_list")
                data = cursor.fetchall()
                for row in data:
                    movie = Movie()
                    movie.title = row[0]
                    movie.year = row[1]
                    movie.director = row[2]
                    movies.append(movie)
        except Exception as e:
            print(f"Error loading movies: {e}")
        return movies



    def save_movies(self, filename):
        with open(filename, "w") as f:
            for movie in self._movies:
                f.write(f"{movie.get_title()},{movie.get_director()},{movie.get_year()}\n")

    def search_by_title(self, title):
        for movie in self._movies:
            if title.lower() in movie.get_title().lower():
                idx = self._movies.index(movie)
                return movie, idx
        return None

    def search_movies(self, query):
        results = []
        for idx, movie in enumerate(self._movies):
            if query.lower() in movie.get_title().lower() or query.lower() in movie.get_director().lower():
                results.append(movie)
        return results

    def add_movie(self, title, director, year):
        movie_object = Movie(title.strip(), director.strip(), year.strip())
        self._movies.append(movie_object)
        self.save_movies(self._filename)

    def remove_movie(self, query):
        if query.isdigit():
            idx_to_remove = int(query) - 1
            if 0 <= idx_to_remove < len(self._movies):
                removed_movie = self._movies.pop(idx_to_remove)
                print(f"Successfully removed '{removed_movie.get_title()}'.")
                self.save_movies(self._filename)
            else:
                print(f"Error: Index {idx_to_remove} is invalid.")
        else:
            result = self.search_by_title(query)
            if result is not None:
                movie_to_remove, idx = result
                self._movies.remove(movie_to_remove)
                print(f"Successfully removed '{movie_to_remove.get_title()}'.")
                self.save_movies(self._filename)
            else:
                print(f"Error: Movie with title '{query}' not found.")

    def get_movies(self):
        return self._movies

def get_connection(self):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="movies"
    )
    return mydb

