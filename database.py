from urllib.parse import quote_plus
from pymongo import MongoClient
from sqlalchemy.orm import sessionmaker
from pymongo.collection import Collection

# Replace <username>, <password>, and <database_name> with your actual MongoDB credentials
username = "shivam52nishad"
password = "@Shivasha.1"
database_name = "test"

username = quote_plus(username)
password = quote_plus(password)

DATABASE_URL = f"mongodb+srv://{username}:{password}@cluster0.6m79trp.mongodb.net/{database_name}?retryWrites=true&w=majority"

client = MongoClient(DATABASE_URL)
db = client.get_database()
users_collection: Collection = db.users
blogs_collection: Collection = db.blogs

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=client)

def get_db():
    try:
        yield db
    finally:
        # Close any open connections or resources if needed
        pass