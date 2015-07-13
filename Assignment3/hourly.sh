#!/bin/bash

# this is the script that will run hourly


# This downloads the data
/home/pi/ass3/grab_data.sh

# This will read in the downloaded csv and output a graph
ipython /home/pi/ass3/graph_pedometer.py

