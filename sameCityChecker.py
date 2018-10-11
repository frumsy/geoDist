#this file is a testing file to check if any of the buisnesses that are located in key cities are assigned key cities that are not that said city

import csv

class Buisness:
    def __init__(self, name, street, city, state, zipcode, keyCity):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.keyCity = keyCity
    def getAddress(self):
        return (self.street + ', ' + self.city + ', ' + self.state + ' ' + self.zipcode)
    def toString(self):
        return (self.name + ': ' + self.getAddress())


keyCities = []
buisnesses = []
def loadBuisnesses():
    i = 0
    bs =[]
    with open('up.csv', newline='') as csvfile:
        buisnessReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in buisnessReader:
            bs.append(row)

    for b in bs:
        name = b[0].replace('"', '')
        street = b[1].replace('"', '')
        city = b[2].replace('"', '')
        state = b[3].replace('"', '')
        zipcode = b[4].replace('"', '')
        keyCity = b[7].replace('"','')
        buisnesses.append(Buisness(name, street, city, state, zipcode, keyCity))


loadBuisnesses()
def readKeyCities(fileName):
    kc = []
    with open(fileName, 'r', newline='') as csvfile:
        addressReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in addressReader:
            kc.append(row)
    return kc

keyCities = readKeyCities('CitiesWithCoords.csv')[1:]

kc = []
for x in keyCities:
    kc.append(x[0].split(', ')[0])

count =0
for i,b in enumerate(buisnesses):
    if(b.city in kc):
        if(b.city != b.keyCity):
            count +=1
            print(i, b.city, b.keyCity, count)
            print(b.toString())
