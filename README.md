# Capturing and mapping NOAA data
### ProjectDaniTessel2018
*Written by Danielle Crowley & Tessel Lagerwerf*

It is key to read this file fully before proceding to use any of its associated scripts.

# Description
Data files, such as those from sources like NOAA, contain large amounts of column delimated data, which are often manually processed with a text editor before the data is plotted on a map. The scripts created here are made to capture specific elements of the data files (scientific name, co-ordinates, species type and depth) and to then use this infromation to create annual plotted maps (run from an R script) and then also a kml file, which can be run within Google Earth and provides an in depth look at the plotted data. 

Within the main directory you will find a detailed report on any lines that should be edited before running these scripts on your own data. For these to work you should have access to both R with the required installs (see report) and Google Earth. These scripts were designed for python version 2.7.

## Scripts

1: *LINK HERE*  : Processes the data file and creates the kml file, which can be veiwed with Google Earth

2: *LINK HERE*  : Uses the specified data within the R script to create the annual ggplot maps
