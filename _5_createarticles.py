#
# Lets add a new type of article with a posting date and a section
#

import pymongo
import pprint
import datetime
import sys

if len(sys.argv) > 1 :
    host=sys.argv[1]
else:
    host="mongodb://localhost:27017"

client = pymongo.MongoClient(host=host) # defaults to mongodb://localhost:27017
blogDatabase = client["blog"]
usersCollection = blogDatabase["users"]
articlesCollection = blogDatabase[ "articles" ]

author = "jdrumgoole"
title = "This is a post on MongoDB"

newPost = {"title": title,
           "body": "MongoDB is the worlds most popular NoSQL database. It is a document database",
           "username": author,
           "tags": ["joe", "mongodb", "Ireland"],
           "section": "technology",
           "postDate": datetime.datetime.now(),
           }

#
# Lets check if our author exists
#

if usersCollection.find_one({"username": author}):
    articlesCollection.insert_one(newPost)
    pprint.pprint( newPost )
else:
    raise ValueError("Author %s does not exist as a user" % author)
