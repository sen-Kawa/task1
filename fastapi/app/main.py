from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongo_host = 'mongo'
mongo_port = 27017
mongo_db = 'myDB'
mongo_collection = 'Todos'

client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]

@app.get("/")
def index():
    return {"hello": "world"}

@app.get("/todos")
def read_data():
    collection = db[mongo_collection]
    data = []
    for item_data in collection.find():
        del item_data['_id']
        data.append(item_data)
    return data
