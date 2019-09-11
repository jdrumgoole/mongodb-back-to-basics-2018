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
import sys

from pymongo.errors import ConnectionFailure

if len(sys.argv) > 1 :
    host=sys.argv[1]
else:
    host="mongodb://localhost:27017"

client = pymongo.MongoClient(host=host) # defaults to mongodb://localhost:27017

try:
    # The ismaster command is cheap and does not require auth.
    status = client.admin.command( "ismaster" )
    print(f"mongod server running on {host}")
    pprint.pprint( status )
except ConnectionFailure:
    print( f"MongoDB Server (mongod) not available on {host}" )
