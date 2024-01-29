# FastAPI
## main.py
### Connection
Connects with mongoDB server using pymongo.
### Function definition
Defines a function to be used by all routes in order to .find() the data in a determined collection. Removes the object id which cannot be json serialized.
### Routes
There is a route for each collection including one for the count of a particular user total posts.
