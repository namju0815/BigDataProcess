#!/usr/bin/python3
import sys
inputfile = input()
outfile = input()
f = open(inputfile,'r')
line = f.readline()
genre={'Animation' : 0, "Children's" : 0, 'Comedy' : 0, 'Adventure' : 0, 'Fantasy' : 0, 'Romance' : 0, 'Drama' : 0, 'Action' : 0, 'Crime' : 0, 'Thriller' : 0, 'Horror' : 0, 'Sci-Fi' : 0, 'Documentary' : 0}
keylist = list(genre.keys())

while line:
	fline = line.split("::")
	gline = fline[2].split("|")
	gline = list(map(lambda s: s.strip(), gline))
	for i in gline:
		for k in keylist:
			if(i == k):
				genre[k]+=1
	line = f.readline()

valuelist = list(genre.values())
index = 0

w = open(outfile,'w')
for i in genre:
	data = ('{} {}'.format(keylist[index], valuelist[index]))
	index+=1
	w.write(data)
	w.wrtte('\n')
	
w.close()
f.close()
