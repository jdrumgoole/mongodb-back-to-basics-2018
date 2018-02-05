'''
Created on 23 May 2016

@author: jdrumgoole
'''

import pymongo
import string
import datetime
import random
    
def randomString( size, letters = string.letters ):
    return "".join( [random.choice( letters )  for _ in xrange( size )] )

client  = pymongo.MongoClient()

def makeArticle( count, author, timestamp ):
    
    return { "_id"      : count,  
             "title"    : randomString( 20 ),
             "body"     : randomString( 80 ),
             "author"   : author,
             "postdate" : timestamp }


def makeUser( username ):
    return { "username" : username, 
             "password" : randomString( 10 ) , 
             "karma" : random.randint( 0, 500 ),
             "lang" : "EN" }
#
# Clean database before each run (don't do this in production)
#
client.drop_database( "blog" )

blogDatabase = client[ "blog" ]
usersCollection = blogDatabase[ "users" ]
articlesCollection = blogDatabase[ "articles" ]

bulkUsers = usersCollection.initialize_ordered_bulk_op()
bulkArticles = articlesCollection.initialize_ordered_bulk_op()

ts = datetime.datetime.now()

for i in range( 1000000 ) :
    #username = randomString( 10, string.ascii_uppercase ) + "_" + str( i )
    username = "USER_" + str( i )
    bulkUsers.insert( makeUser( username ) )
    
    ts = ts + datetime.timedelta( seconds =  1 )
    bulkArticles.insert( makeArticle( i, username, ts ))
    
    if ( i % 500 == 0 ) :
        bulkUsers.execute()
        bulkArticles.execute()
        bulkUsers = usersCollection.initialize_ordered_bulk_op()
        bulkArticles = articlesCollection.initialize_ordered_bulk_op()
        
bulkUsers.execute()
bulkArticles.execute()