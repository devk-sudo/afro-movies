# routes/movies.py
from flask import Blueprint, jsonify
from models.movie import Movie

movies_bp = Blueprint("movies", __name__)

@movies_bp.route("/all", methods=["GET"])
def get_all_movies():
    from app import mongo  # Import here, inside the function
    movies = Movie.get_all(mongo)
    return jsonify(movies)

@movies_bp.route("/latest", methods=["GET"])
def get_latest_movies():
    from app import mongo
    movies = Movie.get_latest(mongo)
    return jsonify(movies)

@movies_bp.route("/category/<category>", methods=["GET"])
def get_movies_by_category(category):
    from app import mongo
    movies = Movie.get_by_category(mongo, category)
    return jsonify(movies)

@movies_bp.route("/popular", methods=["GET"])
def get_most_popular():
    from app import mongo
    movies = Movie.get_most_popular(mongo)
    return jsonify(movies)