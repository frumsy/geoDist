import csv
import time
import re
import googlemaps

f = open('mapsAPIKey.txt', 'r')
apiKey = f.read().replace('\n','')
f.close()

gmaps = googlemaps.Client(key=apiKey)

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

def cleanAddress(add):
    return re.sub('^(\s)*((LLC)|(Inc))*(\.*,*)*(\s)*', '', add)

def getCoords(buis):
    add = cleanAddress(buis.getAddress())
    result = gmaps.geocode(add)
    if(len(result) > 0):
        loc = result[0]['geometry']['location']
        lat = loc['lat']
        lng = loc['lng'] 
        return (lat,lng)
    else:
        return None

def mapBuisnesses(companies):
    addressByBuisness = {}
    count = 0
    successCount = 0#number of get attempts for getcoords that succeeded
    for b in companies[1:]:
        count += 1
        b_coords = getCoords(b)
        if(b_coords != None):
            successCount += 1
        addressByBuisness[b] = b_coords
        if(count > 0 and count % 500 == 0):
            writeBuisnesses(addressByBuisness)          
        print(b.toString(), 'coords: ', b_coords)
        print("attempts: ", count, 'success:', successCount, "failed:", count - successCount)
        time.sleep(0.1)
    return addressByBuisness

def writeBuisnesses(buisnessMap):
   with open('googleBuisnessMap.csv', 'w', newline='') as csvfile:
    fieldnames = ['buisness', 'coords']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for b, c in buisnessMap.items():#b = buisness, c = coords
        writer.writerow({'buisness': b.toString(), 'coords': c})
    #writer.writerow({'buisnesses': '', 'coords': ''})

def getPercentSuccess(b_map):
    fails = 0.
    succ = 0.
    for b, c in b_map.items():
        if(c == None):
            fails += 1
        else:
            succ += 1
    total = fails + succ
    return (succ/total)
 
addByBuis = mapBuisnesses(buisnesses)
print("percent success: ", (100*getPercentSuccess(addByBuis)))
writeBuisnesses(addByBuis)
