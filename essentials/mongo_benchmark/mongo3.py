# FastAPI + MongoDB
# Option 3: Use the async Motor library.
import motor.motor_asyncio
from fastapi import FastAPI, status
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
client = motor.motor_asyncio.AsyncIOMotorClient(uri)

@app.get("/movies/{genre}", response_model=List[str])
async def get_movies(genre: str):
    """Get first N movies in the specified genre."""
    movie_collection = client[DB][MSG_COLLECTION]
    cursor = movie_collection.find({"genres": genre}).limit(100)
    movie_title_list = []
    async for msg in cursor:
        movie_title_list.append(msg["title"])
    return movie_title_list
