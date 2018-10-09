import googlemaps

f = open('mapsAPIKey.txt', 'r')
apiKey = f.read().replace('\n','')
f.close()
print(apiKey)

gmaps = googlemaps.Client(key=apiKey)

add = '1601 E 84Th Ave Ste 102, Anchorage, AK 99507'
result = gmaps.geocode(add)

loc = result[0]['geometry']['location']
lat = loc['lat']
lng = loc['lng']
print(lat,lng)
