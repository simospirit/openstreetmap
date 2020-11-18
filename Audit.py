#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

