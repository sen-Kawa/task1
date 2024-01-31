from fastapi import FastAPI, HTTPException
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

def read_data_by_id(item_id, collection_name):
    collection = db[collection_name]
    item =  collection.find_one({"id": item_id})
    if item:
        del item['_id']
        return item
    raise HTTPException(status_code=404, detail="ID not found")

@app.get("/")
def index():
    return {"Task": "Data Engineering and API Development Exercise"}

@app.get("/posts")
def read_posts():
    return read_data('Posts')

@app.get("/posts/{post_id}")
def read_post( post_id: int ):
    return read_data_by_id(post_id, 'Posts')

@app.get("/comments")
def read_comments():
    return read_data('Comments')

@app.get("/comments/{comment_id}")
def read_comment( comment_id: int ):
    return read_data_by_id(comment_id, 'Comments')

@app.get("/albums")
def read_albums():
    return read_data('Albums')

@app.get("/albums/{album_id}")
def read_album( album_id: int ):
    return read_data_by_id(album_id, 'Albums')

@app.get("/photos")
def read_photos():
    return read_data('Photos')

@app.get("/photos/{photo_id}")
def read_photo( photo_id: int ):
    return read_data_by_id(photo_id, 'Photos')

@app.get("/todos")
def read_todos():
    return read_data('Todos')

@app.get("/todos/{todo_id}")
def read_todo( todo_id: int ):
    return read_data_by_id(todo_id, 'Todos')

@app.get("/users")
def read_users():
    return read_data('Users')

@app.get("/users/{user_id}")
def read_user( user_id: int ):
    return read_data_by_id(user_id, 'Users')

@app.get("/count")
def user_stats():
    data = []
    users = db['Users']
    for user in users.find():
        data.append(
            {
                "userId": user["id"],
                "number_posts": count_posts(user["id"]),
                "number_comments": count_comments(user["email"])
            }
        )
    return data

def count_posts(userId):
    posts = db['Posts']
    return posts.count_documents({ "userId": userId })

def count_comments(userEmail):
    comments = db['Comments']
    return comments.count_documents({ "email": userEmail })
