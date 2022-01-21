# shilu-utilities

Created by Ian M. Miller 
@imiller82 

Utilities for working with the Shilu (Vertiable Records).

Currently works only on Ming Shilu, intend to eventually extend to Qing Shilu, potentially Choson Shilok etc.

Best used with included .txt files due to reliance on formatting.

These are utilites developed for my own research. I do not have the time to do extensive support/debugging.


————————

numCN

Utility module
Contains dictionaries and functions for processing Chinese numerals and dates into integers and western dates
————————

**Dictionaries**

reignDict - reign period dictionary - base year is the year before the first year of reign, base year + year number gives year; currently Ming only

numDict - dictionary of Chinese numerals, for converting to integers

ganDict - dictionary of heavenly stems/tiangan/天干 for converting to integers 1-10

zhiDIct - dictionary of earthly branches/dizhi/地支 for converting to integers 1-12

gzDict - dictionary of full ganzhi/干支 hexidecimals for converting to integers 1-60

**Conversion functions**
-Note: for all conversion functions, it is best practice to test the format of input by checking if it is in respective dictionaries above

-Better checks may be implimented in future version

numConvert(cnum) - converts from Chinese numerals <10,000 (万/萬) to integers, takes a string (cnum), returns an integer

wanConvert(cnum) - like numConvert(), but works on numerals < 100,000,000 (伊/億)

bigConvert(cnum) - like numConvert(), but works on numerals < 10^16

dateConvert(cdate) - converts Chinese dates from format reign period + year + month to western calendar + lunar month, takes a string (cdate), returns a string format year/month

yearConvert(cdate) - same as dateConvert() but converts year only and returns as integer

rdateConvert(cdate) - converts Chinese dates to integers, but retains as reign year and lunar month, retuned as string of format year/month

In development: convesion functions for weights and measures, currency

——————

shiluSearch   

A search utility for working with the shilu, creates a list of term matches, the surrounding text, and useful metadata (title, volume, line, date, etc)

Current version 0.12

——————

Search for terms (including regex) in the Ming shilu

Takes arguments on the command line as follows:

  first argument: search term - if not provided, promted on command line
  
  second argument: output filename - if not provided, defaults to "output.csv"
  
  third argument: input file directory path - if not provided, defaults to "./shilu/"
  
  
 -Note: Minimal error checking on command line input.

Outputs (to .csv):
 
 +volume title
 
 +volume number
 
 +line in volume (not counting whitespace) - intended to help users of print volumes locate the entry
 
 +line in file (counting whitespace) - intended to help users of this digital copy locate the entry
 
 +reignYear/lunarMonth
 
 +ganzhiDay
 
 +year (Gregorian calendar)
 
 +filename
  
 +term (as found in text)
 
 +line containing term (as found in text)
 

-Note: Uses formatting to recognize structure - depends heavily on start of line (i.e. regex "^")

——————

shiluSplit

A search/split utility for working with the shilu, creates a list of term matches, the surrounding text, and useful metadata (title, volume, line, date, etc)

Works the same as shiluSearch, but splits the line around the search term. 

Current version 0.11

——————


For example, given the line

安南陈煓遣其通议大夫黎亚夫等来朝贡方物

and the search term "朝贡"

the splitter will break this into three terms: 

朝贡,安南陈煓遣其通议大夫黎亚夫等来,方物 

i.e. search term, segment prior to search term, segment after search term

For lines with multiple occurances of the same search term, it will break into more than two segments


Takes arguments on the command line as follows:

  first argument: search term - if not provided, promted on command line
  
  second argument: output filename - if not provided, defaults to "output.csv"
  
  third argument: input file directory path - if not provided, defaults to "./shilu/"
  
  
 -Note: Minimal error checking on command line input.

Outputs (to .csv):
 
 +volume title
 
 +volume number
 
 +line in volume (not counting whitespace) - intended to help users of print volumes locate the entry
 
 +line in file (counting whitespace) - intended to help users of this digital copy locate the entry
 
 +reignYear/lunarMonth
 
 +ganzhiDay
 
 +year (Gregorian calendar)
 
 +filename
  
 +term (as found in text)
 
 +line segment before term
 
 +line segment(s) after(between) terms
 
 ——————

doubleSearch

NOT WORKING AT PRESENT

A search utility for working with the shilu, creates a list of term matches, the surrounding text, and useful metadata (title, volume, line, date, etc)

Works the same as shiluSearch, but if the first search term is found, searches for a second term in the line

Current version 0.10

——————

Takes arguments on the command line as follows:

  first argument: manadatory search term - if not provided, promted on command line
  
  second argument: optional second search term - if not provided, promted on command line
  
  third argument: output filename - if not provided, defaults to "output.csv"
  
  fourth argument: input file directory path - if not provided, defaults to "./shilu/"
  
  
 -Note: Minimal error checking on command line input.

Outputs (to .csv):
 
 +volume title
 
 +volume number
 
 +line in volume (not counting whitespace) - intended to help users of print volumes locate the entry
 
 +line in file (counting whitespace) - intended to help users of this digital copy locate the entry
 
 +reignYear/lunarMonth
 
 +ganzhiDay
 
 +year (Gregorian calendar)
 
 +filename
  
 +first search term (as found in text)
 
 +second search term (as found in text) or "none" if not found in that line
 
 +line containing first search term
