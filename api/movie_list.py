from api.movie_class import Movie

class MovieList:
    def __init__(self, filename):
        self._filename = filename
        self._movies = self._load_movies()

    def _load_movies(self):
        movies = []
        try:
            with open(self._filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        title, director, year = line.split(',')
                        movie_object = Movie(title.strip(), director.strip(), year.strip())
                        movies.append(movie_object)
        except FileNotFoundError:
            print(f"File '{self._filename}' not found. Starting with empty movie list.")
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