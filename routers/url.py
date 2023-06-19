import pymongo
from fastapi import APIRouter
from bson import ObjectId
from datetime import datetime, timedelta
from models.url_model import Url
from models.user_model import User
from dotenv import load_dotenv
import os
import random
import string
from temp_db import url_store

router = APIRouter()

load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

client = pymongo.MongoClient(
    host=MONGO_HOST,
    port=int(MONGO_PORT),
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    authSource=MONGO_DB_NAME
)

database = client[MONGO_DB_NAME]
url_collection = database["urls"]
user_collection = database["users"]

def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(length))
        if short_url not in url_store:
            return short_url

def is_short_url_exists(custom_alias):
    # Check if the custom_alias already exists
    return url_collection.find_one({"hash": custom_alias})

@router.post("/createUrl")
async def create_url(url: Url):
    # Generate a short URL hash
    if url.custom_alias:
        if is_short_url_exists(url.custom_alias):
            return {"error": "Custom alias already exists"}
        else:
            url.hash = url.custom_alias
    else:
        url.hash = generate_short_url()

    # Insert the URL into the database
    url_dict = url.dict()
    url_dict["_id"] = str(ObjectId())
    url_dict["creation_date"] = datetime.now().isoformat()
    url_dict["expiration_date"] = (
        datetime.now() + timedelta(days=30)
    ).isoformat()
    url_collection.insert_one(url_dict)

    return {"short_url": f"http://yourdomain/{url.hash}"}

@router.delete("/deleteUrl")
async def delete_url(url_key: str):
    # Delete the URL from the database
    result = url_collection.delete_one({"hash": url_key})
    if result.deleted_count > 0:
        return {"message": "URL Removed"}
    else:
        return {"message": "URL not found"}
