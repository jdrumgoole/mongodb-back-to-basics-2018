'''
Created on 17 May 2016

@author: jdrumgoole
'''
import pymongo
  
#
# client defaults to localhost and port 27017. eg MongoClient('localhost', 27017)
client  = pymongo.MongoClient()
blogDatabase = client[ "blog" ]
usersCollection = blogDatabase[ "users" ]

usersCollection.insert_one( { "username" : "jdrumgoole", 
                              "password" : "top secret", 
                              "lang" : "EN" })

user = usersCollection.find_one()

articlesCollection = blogDatabase[ "articles" ]

author = "jdrumgoole"

article = { "title"  : "This is my first post",
            "body"   : "The is the longer body text for my blog post. We can add lots of text here.",
            "author" : author,
            "tags"   : [ "joe", "general", "Ireland", "admin" ]
        }

#
# Lets check if our author exists
#

if usersCollection.find_one( { "username" : author }) :
    articlesCollection.insert_one( article )
else:
    raise ValueError( "Author %s does not exist" % author )