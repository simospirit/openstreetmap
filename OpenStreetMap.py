#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://classroom.udacity.com/courses/ud032/lessons/768058569/concepts/8443086480923
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""



#Downloaded OSM file, using ElementTree to parse through it
import xml.etree.ElementTree as ET  
import pprint
inputfile = 'sample.xml'
tags = {}
#Count number# of element Types
def count_tags(inputfile):
    #Reads XML file: sample.xml and count each XML tag within the document
    
    for _, elemt in ET.iterparse(inputfile):
        tag = elemt.tag
        if tag not in tags:
            tags[tag] = 1
        else:
            tags[tag] += 1
    #returns a Dictionary consist of tag_names:(counts as values)
        
    return tags    

pprint.pprint(count_tags(inputfile))


# In[2]:


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


# In[3]:


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


# In[28]:


"""Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected """
#https://classroom.udacity.com/nanodegrees/nd002-wgu/parts/fa83382c-7342-40a3-aa96-d66f213215d4/modules/5760d578-d3e3-4951-b75d-744b4e6fe923/lessons/3deb3102-0ba1-4684-b4b1-3af4b2e8c533/concepts/54446302850923
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

inputfile = 'sample.xml'
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd": "Road", 
            "N.": "North", 
            "Ave.": "Avenue", 
            "Blvd.": "Boulevard", 
            "Blvd": "Boulevard",
            "Ln": "Lane", 
            "N": "North",            
            "Dr": "Drive",
            "Cir": "Circle",
            "Ct": "Court",
            "Pl":"Place"}


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(inputfile):
    inputfile = open(inputfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(inputfile, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    inputfile.close()
    return street_types


#pprint.pprint(dict(street_types))


def update_name(name, mapping):
    m = street_type_re.search(name)
    street_type = m.group()
    if street_type not in expected: 
        if street_type in mapping.keys():  
            new_street_type = mapping[street_type]
            name = name.replace(street_type, new_street_type)

    return name
street_types = audit(inputfile)

for street_type, ways in street_types.items():  
    for name in ways:
        better_name = update_name(name, mapping)
        print(name, "=>", better_name)


# In[33]:


"""
Your task is to wrangle the data and transform the shape of the data
into the model we mentioned earlier. The output should be a list of dictionaries
that look like this:

{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}

You have to complete the function 'shape_element'.
We have provided a function that will parse the map file, and call the function with the element
as an argument. You should return a dictionary, containing the shaped data for that element.
We have also provided a way to save the data in a file, so that you could use
mongoimport later on to import the shaped data into MongoDB. 

Note that in this exercise we do not use the 'update street name' procedures
you worked on in the previous exercise. If you are using this code in your final
project, you are strongly encouraged to use the code from previous exercise to 
update the street names before you save them to JSON. 

In particular the following things should be done:
- you should process only 2 types of top level tags: "node" and "way"
- all attributes of "node" and "way" should be turned into regular key/value pairs, except:
    - attributes in the CREATED array should be added under a key "created"
    - attributes for latitude and longitude should be added to a "pos" array,
      for use in geospacial indexing. Make sure the values inside "pos" array are floats
      and not strings. 
- if the second level tag "k" value contains problematic characters, it should be ignored
- if the second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
- if the second level tag "k" value does not start with "addr:", but contains ":", you can
  process it in a way that you feel is best. For example, you might split it into a two-level
  dictionary like with "addr:", or otherwise convert the ":" to create a valid key.
- if there is a second ":" that separates the type/direction of a street,
  the tag should be ignored, for example:

<tag k="addr:housenumber" v="5158"/>
<tag k="addr:street" v="North Lincoln Avenue"/>
<tag k="addr:street:name" v="Lincoln"/>
<tag k="addr:street:prefix" v="North"/>
<tag k="addr:street:type" v="Avenue"/>
<tag k="amenity" v="pharmacy"/>

  should be turned into:

{...
"address": {
    "housenumber": 5158,
    "street": "North Lincoln Avenue"
}
"amenity": "pharmacy",
...
}

- for "way" specifically:

  <nd ref="305896090"/>
  <nd ref="1719825889"/>

should be turned into
"node_refs": ["305896090", "1719825889"]
"""

from datetime import datetime
import json  
from bson import json_util

CREATED = ["version", "changeset", "timestamp", "user", "uid"]

def shape_element(element):  
    node = {}
    if element.tag == "node" or element.tag == "way" :
        node['type'] = element.tag

        
        for attrib in element.attrib:

            
            if attrib in CREATED:
                if 'created' not in node:
                    node['created'] = {}
                if attrib == 'timestamp':
                    node['created'][attrib] = datetime.strptime(element.attrib[attrib], '%Y-%m-%dT%H:%M:%SZ')
                else:
                    node['created'][attrib] = element.get(attrib)

            
            if attrib in ['lat', 'lon']:
                lat = float(element.attrib.get('lat'))
                lon = float(element.attrib.get('lon'))
                node['pos'] = [lat, lon]

            
            else:
                node[attrib] = element.attrib.get(attrib)

        
        for tag in element.iter('tag'):
            key   = tag.attrib['k']
            value = tag.attrib['v']
            if not prob_chars.search(key):

                
                if lower_colon.search(key) and key.find('addr') == 0:
                    if 'address' not in node:
                        node['address'] = {}
                    sub_attr = key.split(':')[1]
                    if is_street_name(tag):
                        # Do some cleaning
                        better_name = update_name(name, mapping)
                        node['address'][sub_attr] = better_name
                    else:
                        node['address'][sub_attr] = value

                
                elif not key.find('addr') == 0:
                    if key not in node:
                        node[key] = value
                else:
                    node["tag:" + key] = value

        
        for nd in element.iter('nd'):
            if 'node_refs' not in node:
                node['node_refs'] = []
            node['node_refs'].append(nd.attrib['ref'])

        return node
    else:
        return None


def process_map(inputfile, pretty = False):  
    file_out = "{0}.json".format(inputfile)
    with open(file_out, "w") as fo:
        for _, element in ET.iterparse(inputfile):
            el = shape_element(element)
            if el:
                if pretty:
                    fo.write(json.dumps(el, indent=2, default=json_util.default)+"\n")
                else:
                    fo.write(json.dumps(el, default=json_util.default) + "\n")
                    

process_map(inputfile)  


# In[31]:


import os  
print('The downloaded file is {} MB'.format(os.path.getsize(inputfile)/1.0e6)) 


# In[32]:


print('The json file is {} MB'.format(os.path.getsize(inputfile + ".json")/1.0e6))   


# In[ ]:




