import pymongo
import pprint

client = pymongo.MongoClient()
blogDatabase = client["blog"]
usersCollection = blogDatabase["users"]
articlesCollection = blogDatabase[ "articles" ]

author = "jdrumgoole"

article = { "title"  : "This is my first post",
            "body"   : "The is the longer body text for my blog post. We can add lots of text here.",
            "username" : author,
            "tags"   : [ "joe", "general", "Ireland", "admin" ]
        }

#
# Lets check if our author exists
#

if usersCollection.find_one( { "username" : author }) :
    doc = articlesCollection.insert_one( article )
    pprint.pprint( article )
else:
    raise ValueError( "Author %s does not exist as a user" % author )