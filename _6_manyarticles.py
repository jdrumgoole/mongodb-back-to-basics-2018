import pymongo
import string
import datetime
import random
import sys


def randomString(size, letters=string.ascii_letters):
    return "".join([random.choice(letters) for _ in range(size)])

def makeArticle(count):
    return {"_id": count,
            "title": "Title " + str(count),
            "body": randomString(80),
            "author": "USER_" + str(random.randrange(0, 999999)),
            "postdate": datetime.datetime.now()}

def makeUser(count):
    return {"_id": "USER_" + str(count),
            "password": randomString(10),
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
articlesCollection = blogDatabase["articles"]

articlesCollection.drop()

users = []
count = 0
articles = []

for i in range(6000000):
    articles.append(makeArticle(i))

    if (len(articles) % 1000) == 0:
        articlesCollection.insert_many(articles)
        count = count + 1000
        print("inserted %i articles" % count)
        articles = []

if len(articles) > 0:
    articlesCollection.insert_many(articles)
