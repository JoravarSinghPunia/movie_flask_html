from api.movie_class import Movie
from app import app
from api.movie_list_db import MovieListDB
from flask import jsonify, request, render_template

@app.route('/api/movies', methods=["GET"])
#Returns list of all movies
def load_movies():
    movie_data = MovieListDB()
    movies = [
        {
            "title": movie.get_title(),
            "director": movie.get_director(),
            "year": movie.get_year(),
        }
        for movie in movie_data.load_movies()
    ]
    return render_template("list_movie.html")

#Adds a new movie
@app.route('/api/movies', methods=["POST"])
def create_movie():
    title = request.form.get("title")
    director = request.form.get("director")
    year = request.form.get("year")

    movie_data = MovieListDB()
    m = Movie(title, year, director)
    movie_data.add_movie(m)

    return "Movie added successfully!", 201

#Displays HTML form page to add a new movie
@app.route('/api/add-movie', methods=["GET"])
def add_movie_form():
    return render_template("add_movie.html")

