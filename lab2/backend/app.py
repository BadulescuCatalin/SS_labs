from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

try:
    client.server_info()
    print("Conexiune MongoDB reușită!")
except Exception as e:
    print(f"Eroare la conectarea la MongoDB: {e}")