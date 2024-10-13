from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("DATABASE_URL")
client = MongoClient(url, server_api=ServerApi('1'))

db=client.urlShortner
collection=db['urls']