#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#identifying unique users contribute the to the map area: Melbouren, FL. 
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def process_map(inputfile):  
    users = set()
    for _, element in ET.iterparse(inputfile):
        for e in element:
            if 'uid' in e.attrib:
                users.add(e.attrib['uid'])

    return users
#the function process_map return a set of unique user "uid"
users = process_map(inputfile)  
print('Number of unique users:', len(users)) 

