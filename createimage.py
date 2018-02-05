'''
Created on 17 May 2016

@author: jdrumgoole
'''
import pymongo
import bson
import base64

#
# client defaults to localhost and port 27017. eg MongoClient('localhost', 27017)
#
client  = pymongo.MongoClient()

#
# Clean database before each run (don't do this in production)
#
client.drop_database( "blog" )

blogDatabase = client[ "blog" ]
usersCollection = blogDatabase[ "users" ]



usersCollection.insert_one( { "username" : "jdrumgoole", 
                              "password" : "top secret", 
                              "lang" : "EN" })

user = usersCollection.find_one()

articlesCollection = blogDatabase[ "articles" ]

author = "jdrumgoole"
title  = "This is my first post"

article = { "title"  : title,
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

#
# Now lets add an image to the blog post
#

imgData = None

with  open( "mongodb-logo.jpg" , "rb" ) as imgFile :
    imgData = imgFile.read()

bsonImage = base64.standard_b64encode( imgData )

firstPost = articlesCollection.find_one( { "title" : title } )

firstPost[ "headlineImage" ] = bsonImage

articlesCollection.replace_one( {"title" : title }, firstPost )

newImgData = base64.standard_b64decode( bsonImage )

with open( "new-image.jpg", "wb" ) as imgFile :
    imgFile.write( newImgData )
    
