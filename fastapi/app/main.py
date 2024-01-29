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
    return {"Task": "Data Engineering and API Development Exercise"}

@app.get("/posts")
def read_posts():
    return read_data('Posts')

@app.get("/comments")
def read_comments():
    return read_data('Comments')

@app.get("/albums")
def read_albums():
    return read_data('Albums')

@app.get("/photos")
def read_photos():
    return read_data('Photos')

@app.get("/todos")
def read_todos():
    return read_data('Todos')

@app.get("/users")
def read_users():
    return read_data('Users')

@app.get("/count")
def user_stats():
    data = []
    users = db['Users']
    for user in users.find():
        data.append({"userId": user["id"]})
    return data

# def count_posts(id):
#     posts = db['Posts']
#     posts.count_documents({ "userId": id })

