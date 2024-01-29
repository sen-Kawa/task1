import requests
from pymongo import MongoClient

print('SCRIPT')
mongo_host='mongo'
mongo_port=27017
mongo_db='myDB'
mongo_collection='myCollection'

api_url='https://jsonplaceholder.typicode.com/users'

client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]
collection = db[mongo_collection]

user = { "name": "Alex", "lastname": "Jackson"}
users = db.users
user_id = users.insert_one(user).inserted_id


print('DONE SCRIPT')
