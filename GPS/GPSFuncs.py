# -*- coding: utf-8 -*-
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

'''
I've decided I already don't like playing with EXIF data, it's pretty nasty,
(well, not really)
Anyway, this function extracts the GPS tags from the EXIF data and ignores
everything else.
The image function argument is a PIL Image object, so yeah... remember that.
'''


def getGPSTags(imagePath):
    image = Image.open(imagePath)
    #Get the EXIF data from the image.
    rawEXIF = image._getexif()

    #Somewhere to store the rest of the EXIF data, I might use it one day.
    tags = {}

    #Aaand a place to store the GPS data.
    gpsTags = {}

    for tag, value in rawEXIF.items():
        decoded = TAGS.get(tag,tag)
        tags[decoded] = value

    rawGPS = tags['GPSInfo']

    for gpstag , value in rawGPS.items():
        decoded = GPSTAGS.get(gpstag,gpstag)
        gpsTags[decoded] = value

    #Pull together out return variable that includes both tagsets.
    return {'tags' : tags, 'gps' : gpsTags}







'''
This function converts the rational expression of Deg/Min/Sec in the EXIF data
into rational decimal values.
The input should look like ((deg1, deg2), (min1, min2), (sec1, sec2))
which might look like ((42, 1), (2345, 100), (1333, 1000)) or something like
that.
llValues stands for (l)at (l)ong Values. Keepin' it generic.
To convert these rational expressions into decimal we simply divide the first
number by the second number, SIMPLES!
'''
def getDegMinSec(llValues):
    #The dict that will hold our return values.
    outPut = {}

    #Do the magic to get decimal values from the rational fractions.
    #ie, (26/10) becomes 2.6
    outPut['deg'] = llValues[0][0]/llValues[0][1]
    outPut['min'] = llValues[1][0]/llValues[1][1]
    outPut['sec'] = llValues[2][0]/llValues[2][1]
    return outPut

'''
Converts the Degress, Minutes and Seconds expression of Lat and Long to
decimal.
The input variable 'll' is a list containing values for deg, min and sec,
otherwise known as the output from the getDegMinSec() function.
It also takes a latref and longref argument, these factor in so that we get
the coordinates right depending on the hemisphere we're in (southern, northern
eastern and western)'
'''
def dmsToDecimal(ll, latLonRef):
    #Factoring in for the hemisphere we are in.
    #I'm doing the logic for both NS and EW, so don't get confused.'
    factor = 1
    if latLonRef == 'S' or latLonRef == 'W':
        factor = -1
    return (ll['deg'] + (ll['min']/60) + (ll['sec']/3600)) * factor

