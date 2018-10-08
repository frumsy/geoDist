import csv
from geopy.geocoders import Nominatim
import geopy.distance
import time
import re

f = open('agent_name.txt', 'r')
agent_name = f.read().replace('\n','')
f.close()

class Loc:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
 
class Buisness:
    def __init__(self, name, street, city, state, zipcode):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
    def getAddress(self):
        return (self.street + ', ' + self.city + ', ' + self.state + ' ' + self.zipcode)
    def toString(self):
        return (self.name + ': ' + self.getAddress())


def readBuisnesses(fileName):
    bs = []
    with open(fileName, 'r', newline='') as csvfile:
        addressReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in addressReader:
            bs.append(row)
    return bs

def readKeyCities(fileName):
    kc = []
    with open(fileName, 'r', newline='') as csvfile:
        addressReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in addressReader:
            kc.append(row)
    return kc

def getDistance(c1, c2):
    return geopy.distance.distance(c1,c2).km

def getState(s):#gets the state from a string of syntax "state zipcode"
    return s.split(' ')[1]

def getZipcode(s):
    return s.split(' ')[2][:-1]#the [:-1] deletes the last character because there is a " at the end of the zip in the csv file for each line.
buisnesses = readBuisnesses('TestBuisnessMap.csv')
keyCities = readKeyCities('CitiesWithCoords.csv')
#filter each buisness by city it's in 
#calculate distance to closets city

def cleanState(state):
    return state[1:-1]

def onlyIn(keyCitiesList, state):#filters list by state
    citiesByState = [] 
    for c in keyCitiesList:
        print(cleanState(cleanState(c[1])))
        if(cleanState(c[1]) == state):
            print(c)
            citiesByState.append(c)
    return citiesByState

for x in keyCities:
    print(len(x),x)
#for x in buisnesses[1:]:
#    print(len(x), x)
#    print(getState(x[2]),'ZIP: ' ,getZipcode(x[2]))
