#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import re
import numCN

"""

works as follows:

reads each line of the file

strips information on volume, date, line in file, line in volume into running variables

searches for specified regex term, when found, outputs entire line

output format:

term (as found in text), line, volume title, volume number, line in volume (not counting whitespace),line in file (counting whitespace), reignYear/lunarMonth, ganzhiDay, year, filename

note that line in volume DOES NOT include whitespace lines - it is intended to help users of print volumes locate the entry
	whereas line in file DOES include whitespace lines - it is intended to help users of this digital copy locate the entry

uses formatting to recognize structure - depends heavily on start of line (i.e. regex "^")

"""


##
##    MAKE REGULAR EXPRESSIONS
##

#
#make the volume regex
#

volRE = "^(正文)?\s*" #beginning of line, possible 正文 and leading whitespace
	
#add the volume name
volRE += "大?[明|清|崇祯].*(实录|實錄)"

volRE += "卷之?" #vol

#add the volume number
volRE += "["
numerals = list(numCN.numDict)
while len(numerals) > 0:
	volRE += numerals.pop()
volRE += "]+"

#
#make the gazhi regex
#

gzRE = "("
gz = list(numCN.gzDict)
while len(gz) > 1:
	gzRE += gz.pop() + "|"
gzRE += gz.pop() + ")"

#
#make the date regex
#

dateRE = "^\s*" #beginning of line, possibly leading whitespace

#add the reign periods
dateRE += "("
reigns = list(numCN.reignDict)
while len(reigns) > 1:
	dateRE += reigns.pop() + "|"
dateRE += reigns.pop() + ")"

#add the year
dateRE += "["
numerals = list(numCN.numDict)
while len(numerals) > 0:
	dateRE += numerals.pop()
dateRE += "]+年"

#add the month
dateRE +=	"[春夏秋冬]?[闰润潤閏]?[" #season and intercalary markers
numerals = list(numCN.numDict)
while len(numerals) > 0:
	dateRE += numerals.pop()
dateRE += "]*月"

#add the ganzhi
dateRE += gzRE + "?"


###
###      MAIN CODE
###

slpath = "./shilu/"
outputName = "output.csv"

#check for command-line arguments
#first argument --> search term; 
#second argument --> output filename; 
#third argument --> input file directory
if len(sys.argv) == 1:
	searchTerm = input("Enter a search term: ")
elif len(sys.argv) == 2:
	searchTerm = sys.argv[1]
elif len(sys.argv) == 3:
	searchTerm = sys.argv[1]
	if ".csv" in sys.argv[2] or ".txt" in sys.argv[2]:
		outputName = sys.argv[2]
	else:
		print("Output file name poorly formatted, using default output.csv")
elif len(sys.argv) == 4:
	searchTerm = sys.argv[1]
	if ".csv" in sys.argv[2] or ".txt" in sys.argv[2]:
		outputName = sys.argv[2]
	else:
		print("Output file name poorly formatted, using default output.csv")
	if os.path.exists(sys.argv[3]):
		slpath = sys.argv[3]
	else:
		print("Path not found")
		quit()
else:
	print("Too many arguments")
	quit()

#open output file
fileout = open(outputName, 'w')

files = os.listdir(slpath)
files.sort()



for file in files:
	if os.path.isfile(os.path.join(slpath, file)) and file != ".DS_Store":
		filein = open(os.path.join(slpath, file),'r')

		#initialize variables; -1 or "?" indicate that variable was not assigned due to poorly formated input
		ln = 0 
		vln = 0 
		vol = -1
		rdate = -1
		date = "?"
		ganzhi = "?"
		titl = "?"
	
		for line in filein: 
	
			#increase line numbers
			ln += 1 #ln (line in file) includes whitespace lines
			if line.isspace() != True : 
				vln += 1 #vln (line in volume) does not include whitespace lines
	
			#if there ia a volume number, pull it out and put it in cvol
			v = re.search(volRE, line)
			if v != None:
				ctv = v.group()
				ctv = ctv.strip() #strip whitespace
				ctv = ctv.strip("正文") #strip chapter header markers
				ctv = ctv.strip() #strip whitespace again
				ctv = ctv.strip("终終") #strip chapter end-markers - should be redundant
				vln = 0
				
				#split into title and volume number
				tvSplit = re.split("卷", ctv)
				titl = tvSplit[0]
				cvol = tvSplit[1]
				cvol = cvol.strip("之")
		
				#convert cvol using numConvert()
				if cvol in numCN.numDict:
					vol = numCN.numConvert(cvol)
		
			#if there is a well-formatted date, pull it and put it in cdate
			d = re.search(dateRE, line)
			if d != None:
				cdate = d.group()
				cdate = cdate.strip()
				cdate = cdate.strip("○△")
			
				#strip ganzhi from date, use re.sub not just .sub
				g = re.search(gzRE, cdate)
				if g != None:
					ganzhi = g.group()
					cdate = re.sub(ganzhi, "", cdate)
		
				#convert cdate using dateConvert()
				date = numCN.yearConvert(cdate)
				rdate = numCN.rdateConvert(cdate)
		
			#if there is a ganzhi at the beginning of the line, pull it an put it in ganzhi
			g = re.search("^\s*[○△]?" + gzRE, line)
			if g != None:
				ganzhi = g.group()
				ganzhi = ganzhi.strip() #strip whitespace
				ganzhi = ganzhi.strip("○△") #strip entry markers
		
			#If the line contains the search term, print it with the other info
			t = re.search(searchTerm, line)
			if t != None:
				term = t.group()
				entry = line
				entry = entry.strip() #strip
				entry = entry.strip("○△")
				print(term + "," + entry + "," + titl + "," + str(vol) + "," + str(vln) + "," + str(ln) + "," + str(rdate) + ","  + ganzhi + "," + str(date) + "," + file + "\r")
		
		#close input file
		filein.close()  
	elif file != ".DS_Store":
		print(file + " cannot be opened\r")

# Close output file
fileout.close()
