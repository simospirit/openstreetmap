{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#https://classroom.udacity.com/courses/ud032/lessons/768058569/concepts/8402186170923\n",
    "\"\"\"\n",
    "Your task is to explore the data a bit more.\n",
    "Before you process the data and add it into your database, you should check the\n",
    "\"k\" value for each \"<tag>\" and see if there are any potential problems.\n",
    "\n",
    "We have provided you with 3 regular expressions to check for certain patterns\n",
    "in the tags. As we saw in the quiz earlier, we would like to change the data\n",
    "model and expand the \"addr:street\" type of keys to a dictionary like this:\n",
    "{\"address\": {\"street\": \"Some value\"}}\n",
    "So, we have to see if we have such tags, and if we have any tags with\n",
    "problematic characters.\n",
    "\n",
    "Please complete the function 'key_type', such that we have a count of each of\n",
    "four tag categories in a dictionary:\n",
    "  \"lower\", for tags that contain only lowercase letters and are valid,\n",
    "  \"lower_colon\", for otherwise valid tags with a colon in their names,\n",
    "  \"problemchars\", for tags with problematic characters, and\n",
    "  \"other\", for other tags that do not fall into the other three categories.\n",
    "See the 'process_map' and 'test' functions for examples of the expected format.\n",
    "\"\"\"\n",
    "\n",
    "import re\n",
    "\n",
    "lower_case = re.compile(r'^([a-z]|_)*$')  \n",
    "lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')  \n",
    "prob_chars = re.compile(r'[=\\+/&<>;\\'\"\\?%#$@\\,\\. \\t\\r\\n]')\n",
    "\n",
    "def key_type(element, keys):\n",
    "    #tag's attribute matches a regular express and counts # tags.\n",
    "    if element.tag == \"tag\":\n",
    "        if prob_chars.search(element.attrib['k']):\n",
    "            keys['prob_chars'] +=1\n",
    "            #print element.attrib['k']\n",
    "        elif lower_colon.search(element.attrib['k']):\n",
    "            keys['lower_colon'] +=1\n",
    "        elif lower_case.search(element.attrib['k']):\n",
    "            keys['lower_case'] +=1    \n",
    "        else: \n",
    "            keys['other'] +=1\n",
    "        \n",
    "        \n",
    "    return keys\n",
    "   \n",
    "\n",
    "def process_map(inputfile):  \n",
    "    keys = {\"lower_case\": 0, \"lower_colon\": 0, \"prob_chars\": 0, \"other\": 0}\n",
    "    # Iterates through an XML file and create a Dict of keys/count.\n",
    "\n",
    "    for _, element in ET.iterparse(inputfile):\n",
    "        keys = key_type(element, keys)\n",
    "\n",
    "    return keys\n",
    "\n",
    "keys = process_map(inputfile)  \n",
    "pprint.pprint(keys)  "
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
