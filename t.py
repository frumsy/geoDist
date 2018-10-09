import distanceCalculator as d
#d.getClosestKeyCity(d.buisnesses[5], d.keyCities)
print(d.loadBuisnesses('TestBuisnessMap.csv'))
buises = d.readBuisnesses('TestBuisnessMap.csv')
ind =0
succInd=0
"""
for x in buises[5:]:
    print('\n\n\n')
    if(d.parseBuisness(x).toString() != x[0]):
        print(d.parseBuisness(x).toString(), '!=', x[0])
        print("failed:", ind)
        print('')
        ind+=1
    else:
        print('succ:', succInd)
        succInd +=1
"""
#for c in d.keyCities:
#    print(len(c))

#for b in d.buisnesses:
#    print(len(b))
