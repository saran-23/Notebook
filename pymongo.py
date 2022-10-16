# import pymongo
# from pymongo import MongoClient

# mongo_connection = pymongo.MongoClient('localhost', 27017)
# db = mongo_connection['test']


import pymongo

# CONNECTION
mongo_connect = pymongo.MongoClient('localhost', 27017)

# DATABASE
db = mongo_connect["pymongo"]

# COLLECTION
col = db["employees"]

# DATA (DICT)
data = {
    "name": "Saran",
    "course": "Computer Science",
    "Number": 44646464644
}
# INSERTING DATA TO THE COLLECTION
# insert_data = col.insert_one(data)

# VIEWING COLLECTION
find = col.find_one()
print(find)
