import csv

addresses = []
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
        fullAdd = (add[1] + ', ' + add[2] + ', ' + add[3] + ' ' + add[4]).replace('"','')
        print(fullAdd)

loadKeyCities()
#loadAddresses()
