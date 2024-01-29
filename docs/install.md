# Installation instructions
## Install
```
git clone https://github.com/sen-Kawa/task1.git
```
### Build and Run
```
docker compose build
```
```
docker compose up -d
```

### Use
Execute an interactive shell in the container:
```
docker exec -it [ CONTAINER NAME ] bash
```
Use MongoDB shell `mongosh`.
To view the databases type `show dbs`, to view the collections `show collections` and to view the desired data type `db.[collection name].find()`

[mongosh CRUD Operations Documentation](https://www.mongodb.com/docs/mongodb-shell/crud/)
