from services.user_service import UserService
from models.user import User
from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from secrets import mongo_uri

app = FastAPI()

client = MongoClient()

mongo_client = MongoClient(mongo_uri, server_api=ServerApi('1'))
db = mongo_client.aasher

import routes.user_routes