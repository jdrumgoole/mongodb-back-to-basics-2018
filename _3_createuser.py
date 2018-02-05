import pymongo

#
# client defaults to localhost and port 27017. eg MongoClient('localhost', 27017)
#
# create a single user
#

client = pymongo.MongoClient()
blogDatabase = client["blog"]
usersCollection = blogDatabase["users"]

usersCollection.insert_one({"username": "jdrumgoole",
                            "password": "top secret",
                            "lang": "EN"})

user = usersCollection.find_one()

print(user)
