{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "621451\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/Moroccan/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:9: DeprecationWarning: count is deprecated. Use Collection.count_documents instead.\n",
      "  if __name__ == '__main__':\n"
     ]
    }
   ],
   "source": [
    "#brew services start mongodb-community@4.4 to start the DB server and connect to DB in Terminal\n",
    "import pymongo\n",
    "from pymongo import MongoClient\n",
    "client = MongoClient(\"mongodb://localhost:27017\")\n",
    "db = client[\"openstreetmap\"]\n",
    "melbourne_florida = db[\"melbourne_florida\"]\n",
    "#Number of documents\n",
    "#https://classroom.udacity.com/courses/ud032/lessons/745498943/concepts/7347306510923\n",
    "print(melbourne_florida.find().count())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/Moroccan/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:3: DeprecationWarning: count is deprecated. Use Collection.count_documents instead.\n",
      "  This is separate from the ipykernel package so we can avoid doing imports until\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#https://classroom.udacity.com/courses/ud032/lessons/745498943/concepts/7347306470923\n",
    "#i want to find document that do have a govermentType field.  \n",
    "db.melbourne_florida.find({\"governmentType\" : {\"$exists\" : 1}}).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "778"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(melbourne_florida.distinct('created.user'))  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/Moroccan/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: DeprecationWarning: count is deprecated. Use Collection.count_documents instead.\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "556381"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db.melbourne_florida.find({\"type\":{\"$in\":['node']}}).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/Moroccan/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: DeprecationWarning: count is deprecated. Use Collection.count_documents instead.\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "65070"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db.melbourne_florida.find({\"type\":{\"$in\":['way']}}).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': 'Ian Swire', 'count': 111093}\n",
      "{'_id': 'floridaeditor', 'count': 66009}\n",
      "{'_id': 'Panther37', 'count': 62191}\n",
      "{'_id': 'NE2', 'count': 61076}\n",
      "{'_id': 'chachafish', 'count': 32837}\n",
      "{'_id': 'mahahahaneapneap', 'count': 25559}\n",
      "{'_id': 'LeTopographeFou', 'count': 22796}\n",
      "{'_id': 'grouper', 'count': 21930}\n",
      "{'_id': 'Easky30', 'count': 19119}\n",
      "{'_id': 'GlittrGrl', 'count': 12856}\n"
     ]
    }
   ],
   "source": [
    "#Name and count of contributors. \n",
    "cursor= db.melbourne_florida.aggregate([{\"$group\":{\"_id\":\"$created.user\", \"count\":{\"$sum\":1}}}, {\"$sort\":{\"count\":-1}}, {\"$limit\":10}])\n",
    "for document in cursor:\n",
    "    print(document)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "#count of bars in melbourne based of the match. \n",
    "results = db.melbourne_florida.aggregate([{'$match': {'amenity': 'bar'}}])\n",
    "print(len(list(results)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': None, 'count': 619100}\n",
      "{'_id': 'parking', 'count': 893}\n",
      "{'_id': 'restaurant', 'count': 186}\n",
      "{'_id': 'fountain', 'count': 150}\n",
      "{'_id': 'fast_food', 'count': 142}\n",
      "{'_id': 'place_of_worship', 'count': 131}\n",
      "{'_id': 'school', 'count': 110}\n",
      "{'_id': 'fuel', 'count': 96}\n",
      "{'_id': 'shelter', 'count': 72}\n",
      "{'_id': 'bank', 'count': 50}\n"
     ]
    }
   ],
   "source": [
    "#count for different types of amenities. only the top 10.  \n",
    "results = db.melbourne_florida.aggregate([{\"$group\":{\"_id\":\"$amenity\", \"count\":{\"$sum\":1}}}, {\"$sort\":{\"count\": -1}},{'$limit': 10}])\n",
    "for amenity in results:\n",
    "    print(amenity)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': '32940', 'count': 212}\n",
      "{'_id': '32901', 'count': 165}\n",
      "{'_id': '32907', 'count': 143}\n",
      "{'_id': '32935', 'count': 81}\n",
      "{'_id': '32909', 'count': 69}\n",
      "{'_id': '32904', 'count': 44}\n",
      "{'_id': '32937', 'count': 23}\n",
      "{'_id': '32934', 'count': 21}\n",
      "{'_id': '32950', 'count': 21}\n",
      "{'_id': '32955', 'count': 13}\n",
      "{'_id': '32903', 'count': 13}\n"
     ]
    }
   ],
   "source": [
    "results = db.melbourne_florida.aggregate([{'$match': {'address.postcode': {'$exists': 1}}},  \n",
    "                                {'$group': {'_id': '$address.postcode', \n",
    "                                            'count': {'$sum': 1}}}, \n",
    "                                {'$sort': {'count': -1}}, {'$limit': 11}])\n",
    "for zipcode in results:\n",
    "    print(zipcode)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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