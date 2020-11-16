# OpenStreetMap project was great way to learn and explore MongoDb in parallel with Python. Udacity provides lots great inputs and exemples to complete the project.

lets start with downloading the data from openstreetmap.org website as OSM XML file. Then change it to Json when its already cleaned and audited. finally finished with statistical numbers and data summarizing with Python and MongoDB. 

Chosen Map Area:
I choosed my hometown Melbourne FLorida, its a small city located in central FLorida. Its easier because I'm familiar with the area and street names. 

located my city from the map : https://www.openstreetmap.org/relation/117646 using "EXPORT tab". then using Overpass Api to download the file. 
OMS FIle : https://www.openstreetmap.org/export#map=12/28.1176/-80.6613

It was interesting looking at OSM file and how much infomarion carried, luckily i live in small city, so the file wasn't so large. the sample file is 134.5MB
I started by parsing the data through with ElementTree and count the number of unique element types,also by pulling up tags and attribute values. By looking at the output data from parsing, I uncover multiple problems:
_Abbrevaited Street Names: try to find it and replace them with the full text form. Iterate in each node/way/relation in data
the value of the v attribute.

_Cardinal Directions are abbreviated.

References:
#https://docs.python.org/3/howto/regex.html
#https://classroom.udacity.com/courses/ud032/lessons/768058569/concepts/8755386140923
#https://classroom.udacity.com/courses/ud032/lessons/768058569/concepts/8402186170923
#https://classroom.udacity.com/courses/ud032/lessons/768058569/concepts/8443086480923
https://docs.mongodb.com/manual/aggregation/
https://libraries.io/github/mkuehn10/P3-Wrangle-OpenStreetMap-Data
https://stackoverflow.com/questions/30333020/mongodb-pymongo-aggregate-gives-strange-output-something-about-cursorrege
https://jameskao.me/data-wrangling-with-openstreetmap-and-mongodb/



