#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

