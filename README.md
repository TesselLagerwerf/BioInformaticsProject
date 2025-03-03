# Capturing and mapping NOAA data
### ProjectDaniTessel2018
*Written by Danielle Crowley & Tessel Lagerwerf*

It is key to read this file fully before proceding to use any of its associated scripts.

# Description
Data files, such as those from sources like NOAA, contain large amounts of column delimated data, which are often manually processed with a text editor before the data is plotted on a map. The scripts created here are made to capture specific elements of the data files (scientific name, co-ordinates, species type and depth) and to then use this infromation to create annual plotted maps (run from an R script) and then also a kml file, which can be run within Google Earth and provides an in depth look at the plotted data. 

Within the main directory you will find a detailed report on any lines that should be edited before running these scripts on your own data. For these to work you should have access to both R with the required installs (see report) and Google Earth. These scripts were designed for python version 2.7.12 and R version 3.2.3. 

# Usage
To run the command you have to adjust the following command to your home directory (change tessel) and type it in your terminal:
```
python /home/tessel/BioInformaticsProject/ProjectDaniTessel.py $PWD
``` 
If you do not want the output of the KML, you can change 
```
WriteOutFile = True
```
to 
```
WriteOutFile = False
```
Then the input will be on your terminal.


## Scripts

1: [link to script](https://github.com/TesselLagerwerf/BioInformaticsProject/blob/master/ProjectDaniTessel.py) : Downloads the data file to create a file fitted for the R-script. The R-script creates maps. The script continues to create a KML file, that can be uploaded to google earth. In order for the attached R-script within the Rscripts directory to work, this script has to run


## References

1 - Python Software Foundation. Python Language Reference, version 2.7. Available at http://www.python.org

2 - R version 3.2.3 (2015-12-10) -- "Wooden Christmas-Tree" Copyright (C) 2015 The R Foundation for Statistical Computing Platform: x86_64-pc-linux-gnu (64-bit)

3 - NOAA (2015) National Database for Deep-Sea Corals and Sponges (version 20170324-0). https://deepseacoraldata.noaa.gov/; NOAA Deep Sea Coral Research & Technology Program.

