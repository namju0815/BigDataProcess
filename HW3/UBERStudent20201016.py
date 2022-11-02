#!/usr/bin/python3
import sys
import datetime

def day_week(y,m,d):
	dayList = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	return dayList[datetime.date(y,m,d).weekday()]
inputfile = sys.argv[1]
outputfile = sys.argv[2]

udic = dict()
day = []
with open(inputfile, "r") as fp:
	for line in fp:
		uberlist = line.split(",")
		region = uberlist[0]
		day = uberlist[1].split("/") 
		uberlist[1] = day_week(int(day[2]), int(day[0]), int(day[1]))
		key = region + "," + uber[1]
		vehicle = int(uberlist[2])
		trip = int(uberlist[3])
		if key in udic:
			value = udic[key].split(",")
			vehicle += int(value[0])
			trip += int(value[1])
		udic[key] = str(vehicle) + "," + str(trip)

with open(outputfile, "w") as fp:
	for i in udic.items():
		fp.write("%s %s\n" %(i[0], i[1]))

