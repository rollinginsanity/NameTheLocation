# -*- coding: utf-8 -*-
from GPS import GPSFuncs
from Locality import locality
from os import listdir, path, makedirs
import shutil

directory = "testimages"
savedirectory = "output"
geonamesUser = "" #Geonames user ID goes here.

files = listdir(directory)
locations = {}

if not path.exists(savedirectory):
    makedirs(savedirectory)

for file in files:

    #Bit of code to make sure we're not trying to do this on files other than images.'
    if file[-3:].upper()!="JPG":
        continue

    tags = GPSFuncs.getGPSTags(directory+"\\"+file)

    #print (tags)

    latDMS = GPSFuncs.getDegMinSec(tags['gps']['GPSLatitude'])

    longDMS = GPSFuncs.getDegMinSec(tags['gps']['GPSLongitude'])

    latDec = GPSFuncs.dmsToDecimal(latDMS, tags['gps']['GPSLatitudeRef'])

    longDec = GPSFuncs.dmsToDecimal(longDMS, tags['gps']['GPSLongitudeRef'])

    print (file + " " + str(latDec)+", "+str(longDec))

    place = locality.getLocality(latDec, longDec,geonamesUser)


    if locations.get(place) != None:
        locations[place] += 1
    else:
        locations[place] = 1

    print(locations)

    print(file + " " + place)

    shutil.copy(directory+"\\"+file,savedirectory+"\\"+place+" "+str(locations[place])+".jpg")