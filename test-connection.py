from pymongo import MongoClient
connection = MongoClient()
connection = MongoClient('10.1.0.7', 27017)
db = connection.testdb
collection = db.testcollection
for post in collection.find():
        print post
