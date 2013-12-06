#!/usr/bin/python
import sys,re

def parseDate(text):
	return str(re.split("[\<\>]",text[176])[2]);

def parseSunRiseAndSet(text):
	ras = re.findall("[0-9]{2}\:[0-9]{2}",text[219]);
	return ras;

def parseSunDec(text):
	return re.findall("[0-9\-\:]+",text[194])[0];

def parseMoonRise(text):
	return re.findall("[\*0-9]{2}:[\*0-9]{2}",text[248])[0];

def parseMoonSet(text):
	return re.findall("[\*0-9]{2}:[\*0-9]{2}",text[250])[0];

def parseMoonDec(text):
	return  re.findall("Dec\. ...&deg;",text[244])[0][-8:];

def parseMoonIllumin(text):
	return re.findall("[0-9\.]+",text[241])[0];

def parse(text):
	ret = "<tr><center><td>" + str(i) + "</td><td>" + parseDate(text);
	riseAndset=parseSunRiseAndSet(text);
	ret = ret + "</td><td>" + riseAndset[0] + "</td><td>" + riseAndset[1];
	ret = ret + "</td><td>" + parseSunDec(text);
	ret = ret + "</td><td>" + parseMoonRise(text) + "</td><td>" + parseMoonSet(text);
	ret = ret + "</td><td>" + parseMoonDec(text) + "</td><td>" + parseMoonIllumin(text);
	return ret + "</td></center></tr>";


header="<html><head><title>astronomical dates, produces by akiva</title><style>td{text-align:center;vertical-align:middle;}</style></head><body>\n<table border='1' CELLSPACING='1' CELLPADDING='1' align='center'>";
header=header+"<tr><th>index</th><th>date</th><th>sun rise</th><th>sun set</th><th>sun dc</th><th>moon rise</th><th>moon set</th><th>moon dec</th><th>moon illumin</th></tr>";
footer="</table></body></html>"
print header;
for i in range(1095,0,-1):
	f = open("htmls/"+str(i)+".html","r");
	h=f.readlines();
	print parse(h);
	f.close();
print footer;