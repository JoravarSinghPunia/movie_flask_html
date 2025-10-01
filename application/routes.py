from app import app
from api.movie_list import MovieList
from flask import jsonify, request, render_template

@app.route('/api/movies', methods=["GET"])

#Returns list of all movies
def load_movies():
    movie_data = MovieList("api/movies.txt")
    movies = [
        {
            "title": movie.get_title(),
            "director": movie.get_director(),
            "year": movie.get_year(),
        }
        for movie in movie_data.get_movies()
    ]
    return jsonify(movies)

#Adds a new movie
@app.route('/api/movies', methods=["POST"])
def create_movie():
    title = request.form.get("title")
    director = request.form.get("director")
    year = request.form.get("year")

    movie_data = MovieList("api/movies.txt")
    movie_data.add_movie(title, director, year)

    return "Movie added successfully!", 201

#Displays HTML form page to add a new movie
@app.route('/api/add-movie', methods=["GET"])
def add_movie_form():
    return render_template("add_movie.html")

