from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongo_host = 'mongo'
mongo_port = 27017
mongo_db = 'myDB'

client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]

def read_data(collection_name):
    collection = db[collection_name]
    data = []
    for item_data in collection.find():
        del item_data['_id']
        data.append(item_data)
    return data

@app.get("/")
def index():
    return {"hello": "world"}

@app.get("/todos")
def read_todos():
    return read_data('Todos')


