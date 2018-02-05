'''
Created on 23 May 2016

@author: jdrumgoole
'''
import pymongo

client  = pymongo.MongoClient()

blogDatabase = client[ "blog" ]
usersCollection = blogDatabase[ "users" ]