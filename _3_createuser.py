import pymongo
import sys
import pprint
#
# client defaults to localhost and port 27017. eg MongoClient('localhost', 27017)
#
# create a single user
#
if len(sys.argv) > 1 :
    host=sys.argv[1]
else:
    host="mongodb://localhost:27017"

client = pymongo.MongoClient(host=host) # defaults to mongodb://localhost:27017
blogDatabase = client["blog"]
usersCollection = blogDatabase["users"]

usersCollection.insert_one({"username": "jdrumgoole",
                            "password": "top secret",
                            "lang": "EN"})

user = usersCollection.find_one()

pprint.pprint(user)
