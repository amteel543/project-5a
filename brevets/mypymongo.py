import os
from readline import insert_text

from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

db = client.mydb

collection = db.raceinfo

def brevet_insert(time, distance, control):
    
    inserted = collection.insert_one({"time": time, "distance": distance, "control_list": control})
    
    _id = inserted.inserted_id

    return str(_id)

def brevet_fetch(): 

    race_list = collection.find().sort("_id", -1).limit(1)

    for item in race_list:
    
        return item["time"], item["distance"], item["control_list"]