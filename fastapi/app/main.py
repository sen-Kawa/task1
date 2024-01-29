from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongo_host = 'mongo'
mongo_port = 27017
mongo_db = 'myDB'

client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]

@app.get("/")
def index():
    return {"hello": "world"}

print('TEST FASTAPI')
