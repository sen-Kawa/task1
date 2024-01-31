# FastAPI
## main.py
### Connection
Connects with mongoDB server using pymongo.
### Function definition
- `read_data(collection_name)` uses `.find()`
- `read_data_by_id(item_id, collection_name)` uses `.find_one()`

Both remove the object id which cannot be json serialized.
### Routes
- `/`
- `/photos`
- `/photos/{photo_id}`
- `/albums`
- `/albums/{album_id}`
- `/users`
- `/users/{user_id}`
- `/comments`
- `/comments/{comment_id}`
- `/posts`
- `/posts/{post_id}`
- `/todos`
- `/todos/{todo_id}`
- `/count` Count of a particular user total posts and comments.
