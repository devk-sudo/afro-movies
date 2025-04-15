# models/user.py
from bson import ObjectId

class User:
    @staticmethod
    def create(mongo, username, password):
        user = {"username": username, "password": password, "cart": [], "favorites": [], "downloads": [], "paid": []}
        return mongo.db.users.insert_one(user)

    @staticmethod
    def find_by_username(mongo, username):
        return mongo.db.users.find_one({"username": username})

    @staticmethod
    def update_cart(mongo, user_id, cart):
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"cart": cart}})

    @staticmethod
    def update_favorites(mongo, user_id, favorites):
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"favorites": favorites}})

    @staticmethod
    def add_download(mongo, user_id, movie_id):
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$push": {"downloads": movie_id}})

    @staticmethod
    def add_paid(mongo, user_id, movie_id):
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$push": {"paid": movie_id}})