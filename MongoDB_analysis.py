#!/usr/bin/env python
# coding: utf-8

# In[62]:


#brew services start mongodb-community@4.4 to start the DB server and connect to DB in Terminal
import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["openstreetmap"]
melbourne_florida = db["melbourne_florida"]
#Number of documents
#https://classroom.udacity.com/courses/ud032/lessons/745498943/concepts/7347306510923
print(melbourne_florida.find().count())


# In[63]:


#https://classroom.udacity.com/courses/ud032/lessons/745498943/concepts/7347306470923
#i want to find document that do have a govermentType field.  
db.melbourne_florida.find({"governmentType" : {"$exists" : 1}}).count()


# In[7]:


len(melbourne_florida.distinct('created.user'))  


# In[8]:


db.melbourne_florida.find({"type":{"$in":['node']}}).count()


# In[15]:


db.melbourne_florida.find({"type":{"$in":['way']}}).count()


# In[64]:


#Name and count of contributors. 
cursor= db.melbourne_florida.aggregate([{"$group":{"_id":"$created.user", "count":{"$sum":1}}}, {"$sort":{"count":-1}}, {"$limit":10}])
for document in cursor:
    print(document)


# In[52]:


#count of bars in melbourne based of the match. 
results = db.melbourne_florida.aggregate([{'$match': {'amenity': 'bar'}}])
print(len(list(results)))


# In[61]:


#count for different types of amenities. only the top 10.  
results = db.melbourne_florida.aggregate([{"$group":{"_id":"$amenity", "count":{"$sum":1}}}, {"$sort":{"count": -1}},{'$limit': 10}])
for amenity in results:
    print(amenity)


# In[70]:


results = db.melbourne_florida.aggregate([{'$match': {'address.postcode': {'$exists': 1}}},  
                                {'$group': {'_id': '$address.postcode', 
                                            'count': {'$sum': 1}}}, 
                                {'$sort': {'count': -1}}, {'$limit': 11}])
for zipcode in results:
    print(zipcode)


# In[ ]:




