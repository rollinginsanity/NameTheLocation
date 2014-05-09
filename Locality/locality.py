'''
This script is for using the GeoNames database to get locality information for
the locality of a picture.
'''
import requests

#This function takes a LatLon from the GPSFuncs module and gets a locality from
#geonames.
def getLocality(lat,lon,gnUser):
    query = "http://api.geonames.org/findNearbyJSON?lat="+str(round(lat,5))+"&lng="+str(round(lon,5))+"&username="+gnUser
    response = requests.get(query)
    jsonData = response.json()
    localityData = jsonData['geonames']
    return localityData[0]['toponymName']



