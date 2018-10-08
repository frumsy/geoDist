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
    index = 0
    for c in cities:
        index += 1
        loc = getCoords(c)
        cityStateString = c[0] + ', ' +c[1]
        if(loc != None):
            citiesToCoords[cityStateString] = (loc.latitude, loc.longitude)
            print(index, cityStateString, (loc.latitude, loc.longitude))
        else:
            citiesToCoords[cityStateString] = None
            print(cityStateString, "None", index)
        if(index > 1 and index%50 == 0):
            print("writing",index,"cities.")
            writeCoords(citiesToCoords)
        time.sleep(1.1)
    return citiesToCoords

#print(keyCities)
#print(len(keyCities))
def writeCoords(citiesMap):
    with open('CitiesWithCoords.csv', 'w', newline='') as csvfile:
        fieldnames = ['city_state', 'coords']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for loc, coord in citiesMap.items():
            writer.writerow({'city_state': loc, 'coords': coord})

keyCityMap = mapKeyCities(keyCities)
writeCoords(keyCityMap)
