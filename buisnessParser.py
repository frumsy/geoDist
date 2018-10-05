import csv

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

addresses = []
buisnesses = []
addByBuis = {}#buisness -> address 
keyCities_States = []#list of key cities and states in form (city, state)

def loadKeyCities():
    with open('keyCities.csv', newline='') as csvfile:
        cityReader= csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in cityReader:
           keyCities_States.append(row)
    
    for cs in keyCities_States:
        print(cs[0] + ', ' + cs[1]) 

def loadAddresses():
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
        

#loadKeyCities()
loadAddresses()
