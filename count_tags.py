{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#https://classroom.udacity.com/courses/ud032/lessons/768058569/concepts/8443086480923\n",
    "#!/usr/bin/env python\n",
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"\n",
    "Your task is to use the iterative parsing to process the map file and\n",
    "find out not only what tags are there, but also how many, to get the\n",
    "feeling on how much of which data you can expect to have in the map.\n",
    "Fill out the count_tags function. It should return a dictionary with the \n",
    "tag name as the key and number of times this tag can be encountered in \n",
    "the map as value.\n",
    "\n",
    "Note that your code will be tested with a different data file than the 'example.osm'\n",
    "\"\"\"\n",
    "\n",
    "\n",
    "\n",
    "#Downloaded OSM file, using ElementTree to parse through it\n",
    "import xml.etree.ElementTree as ET  \n",
    "import pprint\n",
    "inputfile = 'sample.xml'\n",
    "tags = {}\n",
    "#Count number# of element Types\n",
    "def count_tags(inputfile):\n",
    "    #Reads XML file: sample.xml and count each XML tag within the document\n",
    "    \n",
    "    for _, elemt in ET.iterparse(inputfile):\n",
    "        tag = elemt.tag\n",
    "        if tag not in tags:\n",
    "            tags[tag] = 1\n",
    "        else:\n",
    "            tags[tag] += 1\n",
    "    #returns a Dictionary consist of tag_names:(counts as values)\n",
    "        \n",
    "    return tags    \n",
    "\n",
    "pprint.pprint(count_tags(inputfile))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
