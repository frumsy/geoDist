import geopy.distance
import time
import csv
f = open('agent_name.txt', 'r')
agent_name = f.read().replace('\n','')
f.close()

class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class Buisness:
    def __init__(self, name, street, city, state, zipcode, location):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.location = location
    def getAddress(self):
        return (self.street + ', ' + self.city + ', ' + self.state + ' ' + self.zipcode)
    def toString(self):
        return (self.name + ': ' + self.getAddress())


buisnesses = []
def loadBuisnesses():
    bs =[]
    with open('b_with_coords.csv', newline='') as csvfile:
        buisnessReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in buisnessReader:
            bs.append(row)
   
    for b in bs:
        name = b[0].replace('"', '')
        street = b[1].replace('"', '')
        city = b[2].replace('"', '')
        state = b[3].replace('"', '')
        zipcode = b[4].replace('"', '')
        location = b[7]#.replace('"','')
        buisnesses.append(Buisness(name, street, city, state, zipcode, location))

def readKeyCities(fileName):
    kc = []
    with open(fileName, 'r', newline='') as csvfile:
        addressReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in addressReader:
            kc.append(row)
    return kc

def getDistance(c1, c2):
    return geopy.distance.distance(c1,c2).km

def onlyIn(lst, state):#filters lst of keyCities by state
    newList = []
    for row in lst:
        rowState = row[0].split(', ')[1]
        if(rowState == state):
            newList.append(row)
    return newList

def writeBuisnesses(buisnessMap):
    with open('buisnessMap.csv', 'w', newline='') as csvfile:
        fieldnames = ['buisness', 'city']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for b, c in buisnessMap.items():#b = buisness, c = city
            writer.writerow({'buisness': b.toString(), 'city': c})



loadBuisnesses()
keyCities = readKeyCities('CitiesWithCoords.csv')[1:]
cityToBuisness = {}
def findClosestCities(bs):
    for b in bs:
        if(b.location=='' or b.location == ' '):
            print('no coords:', b.toString())
            cityToBuisness[b] = ''
        else:
            stateCities = onlyIn(keyCities, b.state)
            if(len(stateCities) > 0):
                distances = [(getDistance(b.location,c[1]),c) for c in stateCities]
                closeCityState = min(distances,key=lambda item:item[0])[1]
                closestCity = closeCityState[0].split(', ')[0]
                cityToBuisness[b] = closestCity
                #print(closestCity)
            else:
                print(b.state)
                cityToBuisness[b] = ''

#for i,x in enumerate(buisnesses):
#    if(x.state == 'HI'):
#        print(i)

#fromId = 3781
#print(len(buisnesses[fromId:]), buisnesses[fromId:][0].toString())
findClosestCities(buisnesses)
writeBuisnesses(cityToBuisness)
