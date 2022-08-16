import pymongo
from pymongo import MongoClient

cluster= MongoClient("mongodb+srv://hillinhank:groupblue@cluster0.ffmxu49.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["new_17_22"]
collection = db["Sec8_county_merged"]

post = {"_id": 4, "name":"bill", "score":6}

results = collection.find({"state_name":"Alabama"})
for x in results:
    print(x)