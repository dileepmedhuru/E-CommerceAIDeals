from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
collection = db["deals"]

def save_deals(deals):
    collection.insert_many(deals)

def get_saved_deals():
    return list(collection.find({}, {"_id": 0}))
