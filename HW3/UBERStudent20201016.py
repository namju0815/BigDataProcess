#!/usr/bin/python3
import sys
from datetime import datetime, date
inputfile = sys.argv[1]
outputfile = sys.argv[2]

f = open(inputfile,'r')
def day_week(date):
	weekday=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	number = date.weekday()
	return weekday[number]
	
w = open(outputfile,'w')
line = f.readline()

number = dict()
llist=[]
while line:
	fline = line.split(",")
	fline = list(map(lambda s: s.strip(), fline))
	i = fline[0]
	if i not in number:
		number[i]=1
	else:
		number[i]+=1
		
	wline = fline[1].split("/")
	wline = list(map(lambda s: s.strip(), wline))
	day = day_week(date(int(wline[2]), int(wline[0]), int(wline[1])))
	llist.append([fline[0], day, fline[2], fline[3]])
	line = f.readline()

llist.sort()
for i in llist:
	data = ('{},{} {},{}'.format(i[0],i[1],i[2],i[3]))
	w.write(data)
	w.write('\n')	
w.close()
f.close()
