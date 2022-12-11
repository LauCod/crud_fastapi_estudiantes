from pymongo import MongoClient
import motor.motor_asyncio

MONGODB_URL = "mongodb+srv://danielrl:amiSophie7813@cluster0.sve9kp6.mongodb.net/?retryWrites=true&w=majority"  # "mongodb+srv://danielrl:SamiSophie7813@cluster0.sve9kp6.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URL)#motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.mision_tic

collection_name = db['vehicles']
