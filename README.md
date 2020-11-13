# openstreetmap project was great way to learn and explore MongoDb in parallel with Python.Udacity provides lot infos and exemples to complete the project.

lets start with downloading the data from openstreetmap.org website as OSM XML file. Then change it to Json when its already cleaned and audited. finally finished with statistical numbers and data summarizing with Python and MongoDB. 

Chosen Map Area:
I choosed Melbourne FLorida, because that the city where i live, its a small city in Brevard county FL. its easier because I'm familiar with the area and street names. 

located my city from the map : https://www.openstreetmap.org/relation/117646 using "EXPORT tab". then using Overpass Api to download the file. 
OMS FIle : https://www.openstreetmap.org/export#map=12/28.1176/-80.6613

It was interesting looking at OSM file and how much infomarion carried, luckily i live in small city, so the file wasn't so large. the sample file is 134.5MB
I started by parsing the data through with ElementTree and count the number of unique element types,also by pulling up tags and attribute values. By looking at the output data from parsing, I uncover multiple problems:
_Abbrevaited Street Names: try to find it and replace them with the full text form. Iterate in each node/way/relation in data
the value of the v attribute.

_Cardinal Directions are abbreviated.



