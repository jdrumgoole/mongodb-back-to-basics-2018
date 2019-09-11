'''
Created on 5 Apr 2017
@author: jdrumgoole
'''

import requests
import pymongo
import json
import sys

if __name__ == '__main__':

    print('''
For this next set of examples we are going to use a public data set.
Lets download the zips.json file. A collection of ZIP codes for 
the US in json format.

This data is hosted on github at :
https://github.com/jdrumgoole/mongdb-back-to-basics-2018/tree/master/data
    ''')

    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = "mongodb://localhost:27017"


    print("Downloading zips")
    r = requests.get("https://raw.githubusercontent.com/jdrumgoole/mongodb-back-to-basics-2018/master/data/zips.json",
                     stream=True)
    with open("zips.json", 'wb') as fd:
        for chunk in r.iter_content(chunk_size=512):
            fd.write(chunk)
    print("Created zips.json")

    print("Importing zips.json into mongodb")

    client = pymongo.MongoClient(host=host)  # defaults to mongodb://localhost:27017
    b2b_database = client["b2b"]
    b2b_database.drop_collection("zips")
    zips_collection = b2b_database["zips"]

    count = 0
    with open("zips.json", "r") as fd:
        for line in fd:
            line = line[:-1]  # clip \n
            doc = json.loads(line)  # convert to a dict object
            zips_collection.insert_one(doc)
            count = count + 1
            #print( "%i. %s" % ( count, line))

    print("Inserted %i documents" % zips_collection.count())
