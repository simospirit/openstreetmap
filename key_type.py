#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://classroom.udacity.com/courses/ud032/lessons/768058569/concepts/8402186170923
"""
Your task is to explore the data a bit more.
Before you process the data and add it into your database, you should check the
"k" value for each "<tag>" and see if there are any potential problems.

We have provided you with 3 regular expressions to check for certain patterns
in the tags. As we saw in the quiz earlier, we would like to change the data
model and expand the "addr:street" type of keys to a dictionary like this:
{"address": {"street": "Some value"}}
So, we have to see if we have such tags, and if we have any tags with
problematic characters.

Please complete the function 'key_type', such that we have a count of each of
four tag categories in a dictionary:
  "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
See the 'process_map' and 'test' functions for examples of the expected format.
"""

import re

lower_case = re.compile(r'^([a-z]|_)*$')  
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')  
prob_chars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_type(element, keys):
    #tag's attribute matches a regular express and counts # tags.
    if element.tag == "tag":
        if prob_chars.search(element.attrib['k']):
            keys['prob_chars'] +=1
            #print element.attrib['k']
        elif lower_colon.search(element.attrib['k']):
            keys['lower_colon'] +=1
        elif lower_case.search(element.attrib['k']):
            keys['lower_case'] +=1    
        else: 
            keys['other'] +=1
        
        
    return keys
   

def process_map(inputfile):  
    keys = {"lower_case": 0, "lower_colon": 0, "prob_chars": 0, "other": 0}
    # Iterates through an XML file and create a Dict of keys/count.

    for _, element in ET.iterparse(inputfile):
        keys = key_type(element, keys)

    return keys

keys = process_map(inputfile)  
pprint.pprint(keys)  

