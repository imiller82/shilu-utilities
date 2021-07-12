#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


#### DICTIONARIES #####

#reign period dictionary - base year is the year before the first year of reign, base year + year number gives year

reignDict = {
	"洪武" : 1367,
	"建文" : 1398,
	"永乐" : 1402,
	"永樂" : 1402,
	"洪熙" : 1424,
	"宣德" : 1425,
	"正统" : 1435,
	"正統" : 1435,
	"景泰" : 1449,
	"天顺" : 1456,
	"成化" : 1464,
	"弘治" : 1487,
	"正德" : 1505,
	"嘉靖" : 1521,
	"隆庆" : 1566,
	"隆慶" : 1566,
	"万历" : 1572,
	"萬曆" : 1572,
	"泰昌" : 1619,
	"天啟" : 1620,
	"天啓" : 1620,
	"崇祯" : 1627
}

numDict = {
	"" : 0,  # if a number is split and there is no second digit, then it must end in zero (e.g. 十 = 10， 三十 = 30 etc)
	"零" : 0,
	"令" : 0,
	"一" : 1,
	"壹" : 1,
	"元" : 1, #allows for years
	"正" : 1, #allows for months
	"二" : 2,
	"貳" : 2,
	"贰" : 2,
	"两" : 2,
	"兩" : 2,
	"三" : 3,
	"參" : 3,
	"叁" : 3,
	"参" : 3,
	"四" : 4,
	"肆" : 4,
	"五" : 5,
	"伍" : 5,
	"六" : 6,
	"陸" : 6,
	"陆" : 6,
	"七" : 7,
	"柒" : 7,
	"八" : 8,
	"捌" : 8,
	"九" : 9,
	"玖" : 9,
	"十" : 10, # > 9 numerals not used in most functions below, but included for other purposes
	"拾" : 10,
	"廿" : 20,
	"卅" : 30,
	"百" : 100,
	"佰" : 100,
	"千" : 1000,
	"萬" : 10000,
	"万" : 10000,
	"亿" : 100000000,
	"億" : 100000000
}

ganDict = {
	"甲" : 1,
	"乙" : 2,
	"丙" : 3,
	"丁" : 4,
	"戊" : 5,
	"己" : 6,
	"庚" : 7,
	"辛" : 8,
	"壬" : 9,
	"癸" : 10
}

zhiDict = {
	"子" : 1,
	"丑" : 2,
	"寅" : 3,
	"卯" : 4,
	"辰" : 5,
	"巳" : 6,
	"午" : 7,
	"未" : 8,
	"申" : 9,
	"酉" : 10,
	"戌" : 11,
	"亥" : 12
}

gzDict = {
	"甲子" : 1, 
	"乙丑" : 2, 
	"丙寅" : 3, 
	"丁卯" : 4, 
	"戊辰" : 5, 
	"己巳" : 6, 
	"庚午" : 7, 
	"辛未" : 8, 
	"壬申" : 9, 
	"癸酉" : 10, 
	"甲戌" : 11, 
	"乙亥" : 12, 
	"丙子" : 13, 
	"丁丑" : 14, 
	"戊寅" : 15, 
	"己卯" : 16, 
	"庚辰" : 17, 
	"辛巳" : 18, 
	"壬午" : 19, 
	"癸未" : 20, 
	"甲申" : 21, 
	"乙酉" : 22, 
	"丙戌" : 23, 
	"丁亥" : 24, 
	"戊子" : 25, 
	"己丑" : 26, 
	"庚寅" : 27, 
	"辛卯" : 28, 
	"壬辰" : 29, 
	"癸巳" : 30, 
	"甲午" : 31, 
	"乙未" : 32, 
	"丙申" : 33, 
	"丁酉" : 34, 
	"戊戌" : 35, 
	"己亥" : 36, 
	"庚子" : 37, 
	"辛丑" : 38, 
	"壬寅" : 39, 
	"癸卯" : 40, 
	"甲辰" : 41, 
	"乙巳" : 42, 
	"丙午" : 43, 
	"丁未" : 44, 
	"戊申" : 45, 
	"己酉" : 46, 
	"庚戌" : 47, 
	"辛亥" : 48, 
	"壬子" : 49, 
	"癸丑" : 50, 
	"甲寅" : 51, 
	"乙卯" : 52, 
	"丙辰" : 53, 
	"丁巳" : 54, 
	"戊午" : 55, 
	"己未" : 56, 
	"庚申" : 57, 
	"辛酉" : 58, 
	"壬戌" : 59, 
	"癸亥" : 60
}



#### CONVERSION FUNCTIONS ####

#numConvert - takes a Chinese numeral less than 万 (10,000) as a string and returns an integer

def numConvert(cnum):
	num = 0
	
	#check for thousands place
	if "千" in cnum:
		dig = cnum.split("千")
		if dig[0] == "":     #fixes numbers where 一 is not written in the thousands place
			num = num + 1000
		num = num + numDict[dig[0]] * 1000
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
	elif "仟" in cnum:
		dig = cnum.split("仟")
		if dig[0] == "":     #fixes numbers where 一 is not written in the thousands place
			num = num + 1000
		num = num + numDict[dig[0]] * 1000
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros

	#check for hundreds place
	if "百" in cnum:
		dig = cnum.split("百")
		if dig[0] == "":     #fixes numbers where 一 is not written in the hundreds place
			num = num + 100
		num = num + numDict[dig[0]] * 100
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
	elif "佰" in cnum:
		dig = cnum.split("佰")
		if dig[0] == "":     #fixes numbers where 一 is not written in the hundreds place
			num = num + 100
		num = num + numDict[dig[0]] * 100
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
		
	#check for tens place
	if "十" in cnum:
		dig = cnum.split("十")
		if dig[0] == "":     #fixes numbers where 一 is not written in the ten's place
			num = num + 10
		num = num + numDict[dig[0]] * 10
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
	elif "拾" in cnum:
		dig = cnum.split("拾")
		if dig[0] == "":     #fixes numbers where 一 is not written in the ten's place
			num = num + 10
		num = num + numDict[dig[0]] * 10
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
	elif "廿" in cnum:
		dig = cnum.split("廿")
		num = num + 20
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
	elif "卅" in cnum:
		dig = cnum.split("卅")
		num = num + 30
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros

	#add remaining ones place		
	num = num + numDict[cnum]
	return num
	
#wanConvert - takes a Chinese numeral greater than 万/萬 and returns an integer; used in bigConvert

def wanConvert(cnum):
	num = 0
	cnum = cnum.strip("令零") #strip zeros
	
	#check for ten-thousands place
	#简体字
	if "万" in cnum:
		dig = cnum.split("万")
		if dig[0] == "":     #fixes numbers where 一 is not written in the ten-thousands place
			num = num + 10000
		num = num + numConvert(dig[0]) * 10000 #thousands conversion on ten-thousands
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
		
	#繁体字
	if "萬" in cnum:
		dig = cnum.split("萬")
		if dig[0] == "":     #fixes numbers where 一 is not written in the ten-thousands place
			num = num + 10000
		num = num + numConvert(dig[0]) * 10000 #thousands conversion on ten-thousands
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
	
	#convert remainder < 10k
	num = num + numConvert(cnum)
	return num

#bigConvert - large number converter - takes numbers up to but not including 10^16

def bigConvert(cnum):
	num = 0
	cnum = cnum.strip("令零") #strip zeros
	
	#check for hundred-millions place
	#简体字
	if "亿" in cnum:
		dig = cnum.split("亿")
		if dig[0] == "":     #fixes numbers where 一 is not written in the ten-thousands place
			num = num + 100000000
		num = num + wanConvert(dig[0]) * 100000000 #ten thousands conversion on 100 millions
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
	#繁体字
	if "億" in cnum:
		dig = cnum.split("億")
		if dig[0] == "":     #fixes numbers where 一 is not written in the ten-thousands place
			num = num + 100000000
		num = num + wanConvert(dig[0]) * 100000000 #ten thousands conversion on 100 millions
		cnum = dig[1]
		cnum = cnum.strip("令零") #strip zeros
	
	#convert remainder < 100 mil
	num = num + wanConvert(cnum)
	return num

#dateConvert - converts Chinese dates from format reign period + year + month to western calendar + lunar month

def dateConvert(cdate):
	#get the base year (first year of reign - 1) using reignDict
    reignName = cdate[0:2]
    baseYear = reignDict[reignName]
    	
    #put the rest of the date into the remainder and split into year and month
    rem = cdate[2:len(cdate)]
    ym = rem.split('年')
    reignYear = ym[0]
    if len(ym) == 2:
    	cmonth = ym[1]
    else:
    	cmonth = ""
    
    #year is baseYear + converted reignYear
    year = baseYear + numConvert(reignYear)
    
    #check for intercalary months 潤月
    if "閏" in cmonth or "闰" in cmonth or "润" in cmonth or "潤" in cmonth:
    	rn = "r"
    else:
    	rn = ""
    
    #strip non-numerals from month
    cmonth = cmonth.strip("润潤闰閏月春夏秋冬")
    month = numConvert(cmonth)
    date = str(year) + "/" + str(month) + rn
    return date

#yearConvert - same as dateConvert() but converts year only and returns as integer

def yearConvert(cdate):
	#get the base year (first year of reign - 1) using reignDict
    reignName = cdate[0:2]
    baseYear = reignDict[reignName]
    	
    #put the rest of the date into the remainder and split into year and month
    rem = cdate[2:len(cdate)]
    ym = rem.split('年')
    reignYear = ym[0]
    if len(ym) == 2:
    	cmonth = ym[1]
    else:
    	cmonth = ""
    
    #year is baseYear + converted reignYear
    year = baseYear + numConvert(reignYear)
    
    date = year
    return date


#rdateConvert - converts Chinese dates to integers, but retains as reign year and lunar month

def rdateConvert(cdate):
	#get the base year (first year of reign - 1) using reignDict
    reignName = cdate[0:2]
    baseYear = reignDict[reignName]
    	
    #put the rest of the date into the remainder and split into year and month
    rem = cdate[2:len(cdate)]
    
	#split into year and month
    ym = rem.split('年')
    
    #convert the year
    year = numConvert(ym[0])
    
    #check for missing months
    if len(ym) == 2:
    	cmonth = ym[1]
    else:
    	cmonth = ""
    
    #check for intercalary months 潤月
    if "閏" in cmonth or "闰" in cmonth or "润" in cmonth or "潤" in cmonth:
    	rn = "r"
    else:
    	rn = ""
    
    #strip non-numerals from month
    cmonth = cmonth.strip("润潤闰閏月春夏秋冬")
    month = numConvert(cmonth)
    date = str(year) + "/" + str(month) + rn
    return date