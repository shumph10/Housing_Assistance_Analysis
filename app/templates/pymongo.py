import pymongo
from pymongo import MongoClient
from config import *

cluster= MongoClint("MONGO_URL")

db = cluster["new_17_22"]
collection = db["Sec8_county_merged"]

collection.find({"state"})