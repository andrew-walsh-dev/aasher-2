from fastapi import FastAPI
from pymongo import MongoClient
from secrets import mongo_uri

app = FastAPI()
mongo_client = MongoClient(mongo_uri)
db = mongo_client.aasher