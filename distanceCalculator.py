import csv
from commonregex import CommonRegex
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
    parse_text = CommonRegex(s)
    return parse_text.street_address

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
        #print(cleanState(cleanState(c[1])))
        if(cleanState(c[1]) == state):
            print(c)
            citiesByState.append(c)
    return citiesByState

def cleanCoords(coord):
    return float(re.findall(r"[-+]?\d*\.\d+|\d+", coord)[0])

def getClosestKeyCity(b, cits):#b = buisness, cits = keyCities
    state = getState(b[2])
    #print(cits)
    #print(b, b[2])
    #print(state)
    citiesInState = onlyIn(cits, state) 
    closest = citiesInState[0]
    smallest_dist = 100000000000
    #print(citiesInState)
    for c in citiesInState:
        if(len(b) == 5):
            #print("DEBUG:",'c:',c[2],c[3],"b:", b[3],b[4])
            b_lat = cleanCoords(b[3])
            b_long = cleanCoords(b[4])
            c_lat = cleanCoords(c[2])
            c_long = cleanCoords(c[3])
            dist = getDistance( (c_lat, c_long), (b_lat, b_long) )
            if(dist < smallest_dist):
                closest = c
                smallest_dist = dist
        else:
            print("no coords",len(b),b)
    return closest

closestCityToBuisness = {}
for b in buisnesses[1:]:
    close = getClosestKeyCity(b, keyCities)
    closestCityToBuisness[b] = close

#for x in keyCities:
#    print(len(x),x)
#for x in buisnesses[1:]:
#    print(len(x), x)
#    print(getState(x[2]),'ZIP: ' ,getZipcode(x[2]))
