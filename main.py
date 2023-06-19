import pymongo
from fastapi import FastAPI
from routers.url import router
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

app = FastAPI()

client = pymongo.MongoClient(
    host=MONGO_HOST,
    port=int(MONGO_PORT),
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    authSource=MONGO_DB_NAME
)

database = client[MONGO_DB_NAME]

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)