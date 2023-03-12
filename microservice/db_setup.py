from pymongo import MongoClient
from app_config import MONGO_URI


def status():
    client = MongoClient(MONGO_URI)
    db = client.get_database("test")
    coll = db.get_collection("naama_users")
    for word in coll.find({}, {"_id": 0}):
        print(word)
    return coll.find()


def get_message():
    msg = ""
    client = MongoClient(MONGO_URI)
    db = client.get_database("test")
    coll = db.get_collection("naama_users")
    for word in coll.find({}, {"_id": 0}):
        msg = word["message"]
        print(msg)
    return msg


def insert(car_num: int, car_type: str, extended_info):
    client = MongoClient(MONGO_URI)
    db = client.get_database("test")
    coll = db.get_collection("naama_users")
    post = {"car_num": car_num, "car_type": car_type, "extended_info": extended_info}
    coll.update_one(filter={"_id": post.get("car_num")}, update={"$set": post}, upsert=True)
