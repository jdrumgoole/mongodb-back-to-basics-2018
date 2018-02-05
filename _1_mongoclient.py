#
# Simplest MongoDB Client
#
# Joe.Drumgoole@mongodb.com
#
# 5-Feb-2017
#
# Start mongod locally before running this program
#


import pymongo
import pprint

from pymongo.errors import ConnectionFailure
client = pymongo.MongoClient() # defaults to mongodb://localhost:27017
try:
    # The ismaster command is cheap and does not require auth.
    status = client.admin.command( "ismaster" )
    print( "mongod server running on localhost:27017" )
    pprint.pprint( status )
except ConnectionFailure:
    print( "MongoDB Server (mongod) not available on localhost:27017" )