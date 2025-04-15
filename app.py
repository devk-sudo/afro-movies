from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from config import Config
from routes.movies import movies_bp
from routes.users import users_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB
mongo = PyMongo(app)

# Test MongoDB connection
if mongo.db is None:
    raise RuntimeError("MongoDB connection failed: mongo.db is None")
try:
    mongo.db.command("ping")
except Exception as e:
    raise RuntimeError(f"Failed to connect to MongoDB: {str(e)}")

# Initialize JWT
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(movies_bp, url_prefix="/api/movies")
app.register_blueprint(users_bp, url_prefix="/api/users")

# Home page route
@app.route("/")
def home():
    return render_template('index.html')

# API documentation route
@app.route("/api")
def api_docs():
    return render_template('api-docs.html')

if __name__ == "__main__":
    app.run(debug=True)