# compose.yaml
## Services
### mongo
Built from [mongo](https://hub.docker.com/_/mongo/) Docker Official Image.
### data_retrieval
Built based on the [Dockerfile](../../data_retrieval_script/Dockerfile)
#### Dockerfile 
- Builds from the official Python base image. 
- Installs python libraries: requests and pymongo.
- Copies the script into the container.
- Gives exectuting rights to the script.
- Runs the script.
