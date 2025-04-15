from pymongo import MongoClient

# MongoDB Atlas connection string (replace <your_password> with the actual password)
uri = "mongodb+srv://brianrotich044:Kipbrian200@cluster0.zcf5y8z.mongodb.net/afromovies?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(uri)

try:
    # Access the 'afromovies' database
    db = client["afromovies"]

    # Define the sample user
    sample_user = {
        "username": "sampleuser",
        "password": "samplepass",  # In production, hash this using bcrypt or similar
        "cart": [],
        "favorites": [],
        "downloads": [],
        "paid": []
    }

    # Insert the sample user into the 'users' collection
    result = db.users.insert_one(sample_user)
    print(f"Sample user added with ID: {result.inserted_id}")

except Exception as e:
    print("Error adding sample user:", e)

finally:
    # Close the MongoDB connection
    client.close()