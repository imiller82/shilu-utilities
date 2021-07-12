# shilu-utilities

Created by Ian M. Miller 
@imiller82 

Utilities for working with the Shilu (Vertiable Records).

Currently works only on Ming Shilu, intend to eventually extend to Qing Shilu, potentially Choson Shilok etc.

Best used with included .txt files due to reliance on formatting.

Provided as-is. 

These are utilites developed for my own research. I do not have the time to do extensive support/debugging for other implimentations.


###
numCN.py

Utility module
Contains dictionaries and functions for processing Chinese numerals and dates into integers and western dates
###

#Dictionaries

reignDict - reign period dictionary - base year is the year before the first year of reign, base year + year number gives year; currently Ming only
numDict - dictionary of Chinese numerals, for converting to integers
ganDict - dictionary of heavenly stems/tiangan/天干 for converting to integers 1-10
zhiDIct - dictionary of earthly branches/dizhi/地支 for converting to integers 1-12
gzDict - dictionary of full ganzhi/干支 hexidecimals for converting to integers 1-60

#Conversion functions
-Note: for all conversion functions, it is best practice to test the format of input by checking if it is in respective dictionaries above
-Better checks may be implimented in future version

numConvert(cnum) - converts from Chinese numerals <10,000 (万/萬) to integers, takes a string (cnum), returns an integer
wanConvert(cnum) - like numConvert(), but works on numerals < 100,000,000 (伊/億)
bigConvert(cnum) - like numConvert(), but works on numerals < 10^16
dateConvert(cdate) - converts Chinese dates from format reign period + year + month to western calendar + lunar month, takes a string (cdate), returns a string format year/month
yearConvert(cdate) - same as dateConvert() but converts year only and returns as integer
rdateConvert(cdate) - converts Chinese dates to integers, but retains as reign year and lunar month, retuned as string of format year/month

In development: convesion functions for weights and measures, currency

###
shiluSearch.py   

A search utility for working with the shilu, creates a list of term matches, the surrounding text, and useful metadata (title, volume, line, date, etc)

###

Search for terms (including regex) in the Ming shilu

Takes arguments on the command line as follows:
  first argument: search term - if not provided, promted on command line
  second argument: output filename - if not provided, defaults to "output.csv"
  third argument: input file directory path - if not provided, defaults to "./shilu/"
  
 -Note: Minimal error checking on command line input.

Outputs (to .csv):
 term (as found in text)
 line
 volume title
 volume number
 line in volume (not counting whitespace) - intended to help users of print volumes locate the entry
 line in file (counting whitespace) - intended to help users of this digital copy locate the entr
 reignYear/lunarMonth
 ganzhiDay
 year (Gregorian calendar)
 filename

-Note: Uses formatting to recognize structure - depends heavily on start of line (i.e. regex "^")
