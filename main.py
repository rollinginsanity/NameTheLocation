# -*- coding: utf-8 -*-
from GPS import GPSFuncs

tags = GPSFuncs.getGPSTags("testimage2.jpg")

#print (tags)

latDMS = GPSFuncs.getDegMinSec(tags['gps']['GPSLatitude'])

print (latDMS)

longDMS = GPSFuncs.getDegMinSec(tags['gps']['GPSLongitude'])

print (longDMS)

latDec = GPSFuncs.dmsToDecimal(latDMS, tags['gps']['GPSLatitudeRef'])

print (latDec)

longDec = GPSFuncs.dmsToDecimal(longDMS, tags['gps']['GPSLongitudeRef'])

print(longDec)

print (str(latDec)+", "+str(longDec))