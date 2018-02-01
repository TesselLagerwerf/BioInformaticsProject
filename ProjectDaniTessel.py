#! /usr/bin/env python

# This is a python script to generate a abundance map based on 

import re
# Installs the library for regular expressions
import os
# Installs the library for using shell commands within Python
import pandas as pd
# Imported pandas, but to make it easier to use, we imported it as pd.
# This means that when we want to use pandas, we can just say pd
import subprocess as sp
# Imports the library called subprocesses as sp

filename = "deep_sea_corals.csv"
# This is a variable called filename where you can put in the name of the file you want to download from the noaa site
os_command = "".join(["curl -k  \"https://ecowatch.ncddc.noaa.gov/erddap/tabledap/",filename,"?VernacularNameCategory%2CScientificName%2CObservationYear%2Clatitude%2Clongitude%2CDepthInMeters%2CDepthMethod&ObservationYear%3E=2005\" -o deep_sea_curl.csv"])
# This is a variable that joins the filename within the noaa site url to get it to download

os.system(os_command)
# The os.system grands the possibility to use the shell command 'curl', which is within the variable os_command
# Therefore this command will download the file with the filename you want from the NOAA site

Data =  "deep_sea_curl.csv"
# Creates the variable called Data based on the earlier downloaded data file: deep_sea_curl.csv

MarMap = open('ggmap.csv','w')
# Creates the variable called MarMap with the possibility to write in a new file called Data 

SpeciesInfo = pd.read_csv(Data)
# Creating the possibility to use the panda package in the Data, when the variable SpeciesInfo is called
latitude = SpeciesInfo['latitude']
longitude = SpeciesInfo['longitude']
depth = SpeciesInfo['DepthInMeters']
year = SpeciesInfo['ObservationYear']
# The variables to the left are now assigned the values of the headers to the left

DataSet = list(zip(longitude,latitude,depth,year))
# This creates a list where the content of the variables in the zip function are merged into one
Dataframe = pd.DataFrame(data = DataSet, columns=['long','lat','dep','year'])
# This creates a dataframe based on the DataSet with x, y, z as headers
Dataframe.to_csv('ggmap.csv',index=False,header=True)
# Makes the dataframe into a csv file, so this can be used in R
MarMap.close()

Rscript = "R/MapsinR.R"
# Creates a variable with the directory to the Rscript needed
sp.call (["R", "--vanilla", Rscript])
# Runs the Rscript 

def regex1(Data):
# This creates a regular expression called regex1 that searches trough Data
	SubFind= r"(-\d+.\d+),(\d+),averaged"
	SubReplace = r"\1,~\2"
	NewFile = re.sub(SubFind,SubReplace,Data)
	# This means that within the NewFile, the regular expression substituded the SubFind with SubReplace within Data
	return NewFile

def regex2(Data):
	SubFinder = r"(-\d+.\d+),(\d+),\w+"
	SubReplaces = r"\1,\2"
	NewFiles = re.sub(SubFinder,SubReplaces,Data)
	# This means that within the NewFiles, the regular expression substituded the SubFinder with SubReplaces within Data
	return NewFiles

OutFileName = Data + ".kml" 
# This creates a statement called OutFileName which adds .kml to the input file. 

WriteOutFile = True 
# This is just a statement that will be used later to check if we want to write a file or print to the screen. 
# It is currently on True which will print a file but changing this to False (in the script itself) will only print the results in the terminal instead of writing them in a new file.

InFile = open(Data, 'r')
# Creates the variable called InFile with the Data variable displayed in it.
# The r makes it possible to read the file

Headstring = '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<kml xmlns=\"http://earth.google.com/kml/2.2\">
<Document>''' 	
# This creates a statement which represents the header in kml format. It contains information like version and
# encoding which will be read by google earth when the output file is read. 
# The <Document> is the opening for the document code, which includes all the information that we will be using. 
# This will be turned off at the end of all the documents in the footer by </Document>. The three ' allow for the string to be continued on other lines. 

if WriteOutFile: 
# This checks if WriteOutFile is True and when it is the following is going to happen:
	OutFile = open(OutFileName, 'w') 
# If it is true, a new file will be created using open() with the name of the OutFileName name and a 'w' which stand for write. 
# This is then stored in a statement which can be recalled to write something in it using .write
	OutFile.write(Headstring) 
# This writes the previously created Headstring into the OutFile
else:
	print Headstring 
# If WriteOutFile is False, Headstring will be printed in the terminal instead of being written into a file

LineNumber = 0
# This creates a variable called LineNumber, and we set it up to 0 to begin with

for Line in InFile:
# For every Line within the InFile the following loop has to be done:
	if LineNumber > 1:
		Line = regex1(Line)
		# Lets the regular expression (regex1) search and replace every Line and sets the new values to Line
		Line = regex2(Line)
		# Lets the regular expression (regex2) search and replace every Line and sets the new values to Line
		Line = Line.strip('\n')
		# Removes the line ending
		ElementList = Line.split(',')
		# Splits all the elements in the line based on when they are separated by a comma and saves these elements in ElementList
		VernacularName = ElementList[0] 
		ScientificName = ElementList[1]
		ObservationYear = ElementList[2]
		Latitude = ElementList[3]
		Latitude = float(Latitude)
		# Makes the latitude value a float value
		Longitude = ElementList[4]
		Longitude = float(Longitude)
		# Makes the longitude value a float value
		Depth = ElementList[5]
		# Every line where there is ElementList[x] creates a variable where that column of the ElementList is added to
		PlacemarkString =''' 
<Placemark>
	<name>%s</name>
	<description>%s\t%s\t%s</description>
	<Point>
		<altitudeMode>absolute</altitudeMode>
		<coordinates>%f, %f, -%s</coordinates>
	</Point>
</Placemark>''' % \
(ScientificName, VernacularName, ObservationYear, Depth, Longitude, Latitude, Depth) 
# This creates a string which is in kml format with the information we obtained inserted into the correct places using %. 
# This creates a placemark for each line which includes the dive, date, depth and coordinates. 
# The subsections are annotated using <> which are turned off with </>
		if WriteOutFile:
		# This checks if WriteOutFile is True and when it is the following is going to happen:
			OutFile.write(PlacemarkString)
			# The PlacemarkString variable is added to the OutFile
		else:
			print PlacemarkString
			# If the WriteOutFile is false, it prints the PlacemarkString in the terminal

	LineNumber += 1 
# After every loop it adds 1 to the variable LineNumber
	
InFile.close()

if WriteOutFile:
# This checks if WriteOutFile is True and when it is the following is going to happen:
	print "Saved", LineNumber,"records from",Data, "as", OutFileName
	# Prints the text Saved 'Linenumber' records from 'Name of the infile' as 'the name of the outfile'
	OutFile.write('\n</Document>\n</kml>\n')
	# Closing the document and kml codes
	OutFile.close() 
	# Closing the file
else:
	print '\n</Document>\n</kml>\n' 
	# If the WriteOutFile is false, it prints the closing markers in the terminal

