# models/movie.py
class Movie:
    @staticmethod
    def get_all(mongo):
        return list(mongo.db.movies.find())

    @staticmethod
    def get_latest(mongo, limit=10):
        return list(mongo.db.movies.find().sort("release_date", -1).limit(limit))

    @staticmethod
    def get_by_category(mongo, category):
        return list(mongo.db.movies.find({"category": category}))

    @staticmethod
    def get_most_popular(mongo, limit=10):
        return list(mongo.db.movies.find().sort("views", -1).limit(limit))