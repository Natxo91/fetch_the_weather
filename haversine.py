{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import radians, cos, sin, asin, sqrt\n",
    "\n",
    "def haversine(lon1, lat1, lon2, lat2):\n",
    "    #convert degrees to radians\n",
    "    lon1 = radians(lon1)\n",
    "    lat1 = radians(lat1)\n",
    "    lon2 = radians(lon2)\n",
    "    lat2 = radians(lat2)\n",
    "    \n",
    "    dlon = lon2 - lon1\n",
    "    dlat = lat2 - lat1\n",
    "    \n",
    "    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2\n",
    "    distance = 2 * asin(sqrt(a)) * 6371 #6371 is the radius of the Earth\n",
    "    return distance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5570.215609963611"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "haversine(74.0059, 40.7128, 0.1278, 51.5074)"
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
