# FastAPI + MongoDB
# Option 2: Use a Single MongoClient.
from pymongo import MongoClient
from fastapi import FastAPI
import os
from typing import List

# Sample Movie Database from Atlas MongoDB
DB = "sample_mflix"
MSG_COLLECTION = "movies"

# Instantiate the FastAPI
app = FastAPI()

uri = "mongodb+srv://%s:%s@%s/sample_mflix?retryWrites=true&w=majority" % (
    os.environ["MONGO_USER"],
    os.environ["MONGO_PASSWORD"],
    os.environ["MONGO_HOST"],
)

# Instantiate the FastAPI
app = FastAPI()
client = MongoClient(uri)

@app.get("/movies/{genre}", response_model=List[str])
def get_movies(genre: str):
    """Get first N movies in the specified genre."""
    movie_collection = client[DB][MSG_COLLECTION]
    msg_list = movie_collection.find({"genres": genre}).limit(100)
    movie_title_list = []
    for msg in msg_list:
        movie_title_list.append(msg["title"])
    return movie_title_list
