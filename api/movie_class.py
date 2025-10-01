class Movie:
    def __init__(self, title, year, director):
        self._director = director
        self._title = title
        self._year = year



    def get_title(self):
        return self._title

    def get_year(self):
        return self._year

    def get_director(self):
        return self._director

    def __str__(self):
        return f"{self._title} ({self._year}) - Director: {self._director}"


