import pymongo
from pymongo import MongoClient

mongo_connection = pymongo.MongoClient('localhost', 27017)
db = mongo_connection['test']