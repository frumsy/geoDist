from geopy.geocoders import Nominatim
import time
f = open('agent_name.txt', 'r')
agent_name = f.read().replace('\n','')
f.close()

geolocator = Nominatim(user_agent=agent_name)

def getCoords(add):
    location = geolocator.geocode(add)
    time.sleep(1.01)
    if(location != None):
        return (location.latitude, location.longitude)
    return None
add = '1601 E 84Th Ave Ste 102, Anchorage, AK 99507' #original
add2= '1601 84Th Ave Ste 102, Anchorage, AK 99507'#without E
add3= '1601 E 84Th Ave, Anchorage, AK 99507'#without ste and number
print(getCoords(add))
print(getCoords(add2))
print(getCoords(add3))

print(getCoords('8163 Highway 119, Alabaster, AL 35007'))
