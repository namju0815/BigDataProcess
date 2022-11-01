#!/usr/bin/python3
import sys
from datetime import datetime, date
inputfile = sys.argv[1]
outputfile = sys.argv[2]

f = open(inputfile,'r')
def day_week(date):
	week=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	number = date.weekday()
	return week[number]
	
w = open(outputfile,'w')
line = f.readline()
while line:
	fline = line.split(",")
	fline = list(map(lambda s: s.strip(), fline))
	wline = fline[1].split("/")
	wline = list(map(lambda s: s.strip(), wline))
	day = day_week(date(int(wline[2]), int(wline[0]), int(wline[1])))
	data = ('{},{} {},{}'.format(fline[0], day, fline[2], fline[3]))
	w.write(data)
	w.write("\n")
	line = f.readline()
	
w.close()
f.close()
