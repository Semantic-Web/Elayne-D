#!/bin/bash

# Downloads the data csv from a public icloud folder setup by me.
# The 'Stepz' keeps track of my steps as well as allows the export of data into a csv.
# Have configured the app to export the data hourly into the public share where this script will download hourly,
# with an offset of 5 minutes.
 
wget -O /home/pi/ass3/data/pedometer_before.csv "https://www.dropbox.com/s/3hh7xo5yzdk6ap8/DateStepsDos.csv?dl=0"

cat /home/pi/ass3/data/pedometer_before.csv | tr "\r" "\n" > /home/pi/ass3/data/pedometer.csv

