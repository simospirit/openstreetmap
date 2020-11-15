
" OpenStreetMap Project: Data Wrangling with MongoDB
Mohammed Bougayou

Map Area: Melbourne, Florida

located my city from the map : https://www.openstreetmap.org/relation/117646
OMS FIle : https://www.openstreetmap.org/export#map=12/28.1176/-80.6613

Project Summary: cleaning the data OpenStreetMap data of Melbourne florida, using python and audit techniques that i learned from Udacity.
Then going to Json format from XML.OSM data, and import the JSON file to MongoDB Database. 

Problems encounter: Street names type and cardinal directions are abbreviated. 

Files Sizes: 
Melbourne_florida.osm -> 134.5 MB
Sample.json -> 213.4 MB

Number of Documents:
#brew services start mongodb-community@4.4 to start the DB server and connect to DB in Terminal.

import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["openstreetmap"]
melbourne_florida = db["melbourne_florida"]
#Number of documents
#https://classroom.udacity.com/courses/ud032/lessons/745498943/concepts/7347306510923
print(melbourne_florida.find().count())"
   ]}
 






