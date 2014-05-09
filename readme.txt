This is a small script to get the locality an image was taken (based off GPS EXIF data)

.

It's not finished yet, but the general process is:

-Loop through a directory of images
-For each image extract any GPS information
-Perform a reverse geocode lookup using geonames to get the locality the picture was taken
-Apply that locality information to the file name.

You will need:

A geonames account set up to make web requests.


-The Python Pillow Library  http://pillow.readthedocs.org/en/latest/

-The Python Requests Library  http://docs.python-requests.org/en/latest/index.html