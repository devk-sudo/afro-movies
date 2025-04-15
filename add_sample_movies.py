from pymongo import MongoClient

# MongoDB Atlas connection string (replace <your_password> with the actual password)
uri = "mongodb+srv://brianrotich044:Kipbrian200@cluster0.zcf5y8z.mongodb.net/afromovies?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(uri)

try:
    # Access the 'afromovies' database
    db = client["afromovies"]

    # Define sample movies with all required details
    sample_movies = [
        {
            "id": "movie1",
            "title": "The Avengers",
            "category": "Action",
            "release_date": "2012-05-04",
            "views": 1500000,
            "posterUrl": "https://example.com/posters/avengers.jpg",
            "rating": 4.8,
            "year": "2012",
            "duration": "2h 23m",
            "genre": "Action, Adventure, Sci-Fi",
            "downloadCount": 500000
        },
        {
            "id": "movie2",
            "title": "Black Panther",
            "category": "Action",
            "release_date": "2018-02-16",
            "views": 1200000,
            "posterUrl": "https://example.com/posters/black_panther.jpg",
            "rating": 4.7,
            "year": "2018",
            "duration": "2h 14m",
            "genre": "Action, Adventure, Sci-Fi",
            "downloadCount": 400000
        },
        {
            "id": "movie3",
            "title": "The Notebook",
            "category": "Drama",
            "release_date": "2004-06-25",
            "views": 800000,
            "posterUrl": "https://example.com/posters/the_notebook.jpg",
            "rating": 4.5,
            "year": "2004",
            "duration": "2h 3m",
            "genre": "Drama, Romance",
            "downloadCount": 300000
        },
        {
            "id": "movie4",
            "title": "Oppenheimer",
            "category": "Drama",
            "release_date": "2023-07-21",
            "views": 2000000,
            "posterUrl": "https://example.com/posters/oppenheimer.jpg",
            "rating": 4.9,
            "year": "2023",
            "duration": "3h 0m",
            "genre": "Biography, Drama, History",
            "downloadCount": 600000
        },
        {
            "id": "movie5",
            "title": "Inception",
            "category": "Sci-Fi",
            "release_date": "2010-07-16",
            "views": 1800000,
            "posterUrl": "https://example.com/posters/inception.jpg",
            "rating": 4.8,
            "year": "2010",
            "duration": "2h 28m",
            "genre": "Action, Sci-Fi, Thriller",
            "downloadCount": 550000
        }
    ]

    # Insert the sample movies into the 'movies' collection
    result = db.movies.insert_many(sample_movies)
    print(f"Sample movies added with IDs: {result.inserted_ids}")

except Exception as e:
    print("Error adding sample movies:", e)

finally:
    # Close the MongoDB connection
    client.close()