import csv
from geopy.geocoders import Nominatim
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

addresses = []
buisnesses = []
addByBuis = {}#buisness -> address 
keyCities_States = []#list of key cities and states in form (city, state)

def loadKeyCities():
    with open('keyCities.csv', newline='') as csvfile:
        cityReader= csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in cityReader:
           keyCities_States.append(row)
    
    #for cs in keyCities_States:
        #print(cs[0] + ', ' + cs[1]) 

def loadBuisnesses():
    with open('DRT_Upwork.csv', newline='') as csvfile:
        addressReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in addressReader:
            addresses.append(row)

    for add in addresses:
        name = add[0].replace('"', '')
        street = add[1].replace('"', '')
        city = add[2].replace('"', '')
        state = add[3].replace('"', '')
        zipcode = add[4].replace('"', '')        
        buisnesses.append(Buisness(name, street, city, state, zipcode))
        #fullAdd = (buisnesses[len(buisnesses) - 1].getAddress())
        #print(fullAdd)        

loadKeyCities()
loadBuisnesses()

testList = buisnesses[1:11]
for t in testList:
    print(t.toString())

geolocator = Nominatim(user_agent=agent_name)
#print('agent_name: ', agent_name)

def cleanAddress(add):
    return re.sub('^(\s)*((LLC)|(Inc))*(\.*,*)*(\s)*', '', add)

def getCoords(buis):
    add = cleanAddress(buis.getAddress())
    location = geolocator.geocode(add)            
    #print(buis.name, " [location:",  buis.getAddress(), "]", location)
    return location

def mapBuisnesses(companies):
    addressByBuisness = {}
    for b in companies:
        b_location = getCoords(b)
        b_coords = None
        if(b_location != None):
            b_coords = (b_location.latitude, b_location.longitude)    
        addressByBuisness[b] = b_coords          
        print(b.toString(), 'coords: ', b_coords)
        time.sleep(1.01)
    return addressByBuisness

def writeBuisnesses(buisnessMap):
   with open('TestBuisnessMap.csv', 'w', newline='') as csvfile:
    fieldnames = ['buisness', 'coords']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for b, c in buisnessMap.items():#b = buisness, c = coords
        writer.writerow({'buisness': b.toString(), 'coords': c})
    #writer.writerow({'buisnesses': '', 'coords': ''})
    
addByBuis = mapBuisnesses(testList)
writeBuisnesses(addByBuis)
#print(len(buisnesses))
#print(getCoords(buisnesses[len(buisnesses)-1]))
