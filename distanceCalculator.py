import csv
from geopy.geocoders import Nominatim
import time

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



buisnesses = readBuisnesses('TestBuisnessMap.csv')
keyCities = readKeyCities('CitiesWithCoords.csv')

#for x in keyCities:
#    print(len(x),x)
#for x in buisnesses:
#    print(len(x), x)
