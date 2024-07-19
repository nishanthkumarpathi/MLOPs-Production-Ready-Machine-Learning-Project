import os
from pymongo import MongoClient

# Retrieve MongoDB credentials and host details from environment variables
mongo_username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
mongo_password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
mongo_db_url = os.getenv('MONGODB_URL')

print(mongo_db_url)

# Database and Collection names
database_name = "US_VISA"
collection_name = "visa_data"

# Connect to the MongoDB database
client = MongoClient(mongo_db_url)
db = client[database_name]
collection = db[collection_name]

# Fetch all documents from the collection and print them
try:
    documents = collection.find()
    for document in documents:
        print(document)
except Exception as e:
    print(f"An error occurred: {e}")


mongo_db_url = os.getenv('MONGODB_URL')

print(mongo_db_url)

# Database and Collection names
database_name = "US_VISA"
collection_name = "visa_data"

# Connect to the MongoDB database
client = MongoClient(mongo_db_url)
db = client[database_name]
collection = db[collection_name]

# Fetch all documents from the collection and print them
try:
    documents = collection.find()
    for document in documents:
        print(document)
except Exception as e:
    print(f"An error occurred: {e}")
