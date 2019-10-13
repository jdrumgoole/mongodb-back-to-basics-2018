import pymongo
import string
import datetime
import random
import sys


def random_string(size, letters=string.ascii_letters):
    return "".join([random.choice(letters) for _ in range(size)])


def make_user(count):
    return {"_id": "USER_" + str(count),
            "password": random_string(10),
            "karma": random.randint(0, 500),
            "registered": datetime.datetime.utcnow(),
            "lang": "EN"}


if len(sys.argv) > 1 :
    host=sys.argv[1]
else:
    host="mongodb://localhost:27017"

client = pymongo.MongoClient(host=host) # defaults to mongodb://localhost:27017

blogDatabase = client["blog"]
usersCollection = blogDatabase["users"]

usersCollection.drop()

users = []
count = 0
articles = []

for i in range(6000000):
    users.append(make_user(i))

    if (len(users) % 1000) == 0:
        usersCollection.insert_many(users)
        count = count + 1000
        print("inserted %i users" % count)
        users = []

if len(users) > 0:
    usersCollection.insert_many(users)
