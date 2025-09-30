import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB URI from .env
MONGO_URI = os.getenv("MONGO_URI")

# Create client
client = MongoClient(MONGO_URI)

# Select database
db = client["student_database"]

print("✅ MongoDB Connection Successful")
