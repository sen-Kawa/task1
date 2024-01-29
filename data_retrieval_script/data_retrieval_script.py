import requests
from pymongo import MongoClient

mongo_host='mongo'
mongo_port=27017
mongo_db='myDB'

client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data.")
        return None

def store_data(data, collection_name):
    collection = db[collection_name]
    if (data):
        result = collection.insert_many(data)
        print("Data stored succesfully.")
    else:
        print("No data to store.")

api_map = {
        'https://jsonplaceholder.typicode.com/posts': 'Posts',
        'https://jsonplaceholder.typicode.com/comments': 'Comments',
        'https://jsonplaceholder.typicode.com/albums': 'Albums',
        'https://jsonplaceholder.typicode.com/photos': 'Photos',
        'https://jsonplaceholder.typicode.com/todos': 'Todos',
        'https://jsonplaceholder.typicode.com/users': 'Users'
}

for api_url, collection_name in api_map.items():
    api_data = fetch_data(api_url)
    store_data(api_data, collection_name)

client.close()
