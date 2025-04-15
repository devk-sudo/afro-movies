# app.py
from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from config import Config
from routes.movies import movies_bp
from routes.users import users_bp

app = Flask(__name__)
app.config.from_object(Config)

# Print the MONGO_URI for debugging
print("MONGO_URI:", app.config.get("MONGO_URI"))

# Initialize MongoDB
mongo = PyMongo(app)

# Test MongoDB connection
if mongo.db is None:
    raise RuntimeError("MongoDB connection failed: mongo.db is None")
try:
    mongo.db.command("ping")  # Sends a ping command to the MongoDB server
    print("Successfully connected to MongoDB!")
except Exception as e:
    raise RuntimeError(f"Failed to connect to MongoDB: {str(e)}")

# Initialize JWT
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(movies_bp, url_prefix="/api/movies")
app.register_blueprint(users_bp, url_prefix="/api/users")

@app.route("/")
def home():
    return "AfroMovies API is running!"

if __name__ == "__main__":
    app.run(debug=True)