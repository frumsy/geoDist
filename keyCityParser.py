import csv
from geopy.geocoders import Nominatim
import time

#class city_state_coord():
    

f = open('agent_name.txt', 'r')
agent_name = f.read().replace('\n','')
f.close()

def loadKeyCities():
    keyCities = []
    with open('keyCities.csv', newline='') as csvfile:
        cityReader= csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in cityReader:
            keyCities.append(row)
    return keyCities

keyCities = loadKeyCities()
print(keyCities)
geolocator = Nominatim(user_agent=agent_name)
def getCoords(city):
    add = city[0] + ', ' + city[1]
    location = geolocator.geocode(add)    
    return location

def mapKeyCities(cities):    
    citiesToCoords = {}
    for c in cities:
        loc = getCoords(c)
        citiesToCoords[c] = loc
        time.sleep(1.01)
        print(c, loc)
    return citiesToCoords

#print(keyCities)
#print(len(keyCities))
def writeCoords(citiesMap):
    with open('CitiesWithCoords.csv', 'w', newline='') as csvfile:
        fieldnames = ['city_state', 'coords']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for loc, coord in buisnessMap.items():
            writer.writerow({'city_state': loc, 'coords': coord})

keyCityMap = mapKeyCities()
writeCoords(keyCityMap)
