import pymongo
import string
import datetime
import random


def randomString(size, letters=string.letters):
    return "".join([random.choice(letters) for _ in xrange(size)])


client = pymongo.MongoClient()


def makeArticle(count, author, timestamp):
    return {"_id": count,
            "title": randomString(20),
            "body": randomString(80),
            "author": author,
            "postdate": timestamp}


def makeUser(username):
    return {"username": username,
            "password": randomString(10),
            "karma": random.randint(0, 500),
            "registered" : datetime.datetime.utcnow(),
            "lang": "EN"}


blogDatabase = client["blog"]
usersCollection = blogDatabase["users"]
articlesCollection = blogDatabase["articles"]

usersCollection.drop()
articlesCollection.drop()

ts = datetime.datetime.now()

users = []
count = 0
for i in range(1000000):
    username = "USER_" + str(i)

    users.append( makeUser( username ))

    if ( len( users ) % 1000  ) == 0 :
        usersCollection.insert_many( users )
        count = count + 1000
        print( "inserted %i users" % count )
        users = []

articles = []
count = 0

for i in range( 1000000) :
    username = "USER_" + str( random.randrange( 0, 999999 ))
    ts = ts + datetime.timedelta(seconds=1)
    articles.append( makeArticle(i, username, ts))

    if (len( articles ) % 1000 ) == 0 :
        articlesCollection.insert_many( articles )
        count = count + 1000
        print( "inserted %i articles" % count )
        articles = []

