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

def fetch_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data.")
        return None

def store_data(data):
    if (data):
        result = collection.insert_many(data)
        print("Data stored succesfully.")
    else:
        print("No data to store.")


api_data = fetch_data()
store_data(api_data)
client.close()

print('DONE SCRIPT')
