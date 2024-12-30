# 📦 Importing db & env modules
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# 🌐 Load environment variables
load_dotenv()

# 📡 MongoDB connection URL
MONGODB_URI = os.getenv("MONGODB_URL")

# 🌍 Initialize MongoDB client and connect to the database
client = AsyncIOMotorClient(MONGODB_URI, serverSelectionTimeoutMS=2000)
db = client["metryflow"]
metrics_collection = db["metrics"]
