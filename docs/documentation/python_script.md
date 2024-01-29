# Python Script Documentation
## Overview
This Python script fetches data from various endpoints of the JSONPlaceholder API and stores it in corresponding collections within a defined MongoDB database.

### Libraries
- **requests** is used for the API requests.
- **pymongo** is used to interact with MongoDB.

### Functions
- `fetch_data(api_url)` sends a GET request to the specified endpoint in the parameter.
- `store_data(data, collection_name)` creates a MongoDB collection with the data fetched and names it accordingly.

### API Mapping
`api_map` is a dictionary that maps the API endpoints to collection names.
