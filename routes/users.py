# routes/users.py
from flask import Blueprint, request, jsonify, session
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import User
from bson import ObjectId

users_bp = Blueprint("users", __name__)

@users_bp.route("/register", methods=["POST"])
def register():
    from app import mongo
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")  # Hash this in production
    if User.find_by_username(mongo, username):
        return jsonify({"message": "Username already exists"}), 400
    User.create(mongo, username, password)
    return jsonify({"message": "User created"}), 201

@users_bp.route("/login", methods=["POST"])
def login():
    from app import mongo
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = User.find_by_username(mongo, username)
    if user and user["password"] == password:  # Compare hashed passwords in production
        # Merge session cart/favorites with user account
        session_cart = session.get("cart", [])
        session_favorites = session.get("favorites", [])
        if session_cart:
            User.update_cart(mongo, user["_id"], session_cart)
            session.pop("cart", None)
        if session_favorites:
            User.update_favorites(mongo, user["_id"], session_favorites)
            session.pop("favorites", None)
        access_token = create_access_token(identity=str(user["_id"]))
        return jsonify({"access_token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@users_bp.route("/cart", methods=["GET", "POST"])
@jwt_required(optional=True)
def manage_cart():
    from app import mongo
    user_id = get_jwt_identity()
    if request.method == "POST":
        data = request.get_json()
        movie_id = data.get("movie_id")
        if user_id:  # Logged-in user
            user = User.find_by_username(mongo, mongo.db.users.find_one({"_id": ObjectId(user_id)})["username"])
            cart = user.get("cart", [])
            cart.append(movie_id)
            User.update_cart(mongo, user_id, cart)
        else:  # Anonymous user
            cart = session.get("cart", [])
            cart.append(movie_id)
            session["cart"] = cart
        return jsonify({"message": "Added to cart"}), 200
    # GET request
    if user_id:
        user = User.find_by_username(mongo, mongo.db.users.find_one({"_id": ObjectId(user_id)})["username"])
        return jsonify(user.get("cart", []))
    return jsonify(session.get("cart", []))

@users_bp.route("/favorites", methods=["GET", "POST"])
@jwt_required(optional=True)
def manage_favorites():
    from app import mongo
    user_id = get_jwt_identity()
    if request.method == "POST":
        data = request.get_json()
        movie_id = data.get("movie_id")
        if user_id:
            user = User.find_by_username(mongo, mongo.db.users.find_one({"_id": ObjectId(user_id)})["username"])
            favorites = user.get("favorites", [])
            favorites.append(movie_id)
            User.update_favorites(mongo, user_id, favorites)
        else:
            favorites = session.get("favorites", [])
            favorites.append(movie_id)
            session["favorites"] = favorites
        return jsonify({"message": "Added to favorites"}), 200
    if user_id:
        user = User.find_by_username(mongo, mongo.db.users.find_one({"_id": ObjectId(user_id)})["username"])
        return jsonify(user.get("favorites", []))
    return jsonify(session.get("favorites", []))

@users_bp.route("/account", methods=["GET"])
@jwt_required()
def get_account():
    from app import mongo
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return jsonify({
        "username": user["username"],
        "downloads": user.get("downloads", []),
        "paid": user.get("paid", []),
        "favorites": user.get("favorites", []),
        "cart": user.get("cart", [])
    })