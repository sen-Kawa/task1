# Installation instructions
## Install
```
git clone https://github.com/sen-Kawa/task1.git
```
### Build and Run
```
docker compose up --build
```

Access FastAPI in your browser `0.0.0.0:8000/docs`
#### Available routes
```
0.0.0.0:8000/
```
```
0.0.0.0:8000/posts
```
```
0.0.0.0:8000/comments
```
```
0.0.0.0:8000/albums
```
```
0.0.0.0:8000/photos
```
```
0.0.0.0:8000/todos
```
```
0.0.0.0:8000/users
```
```
0.0.0.0:8000/count
```

### To interact with MongoDB
```
docker compose up --build -d
```
Execute an interactive shell in the container:
```
docker exec -it mongo bash
```
Use MongoDB shell `mongosh`.
To view the databases type `show dbs`, to view the collections `show collections` and to view the desired data type `db.[collection name].find()`

[mongosh CRUD Operations Documentation](https://www.mongodb.com/docs/mongodb-shell/crud/)
