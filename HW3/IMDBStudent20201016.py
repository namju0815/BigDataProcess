#!/usr/bin/python3
import sys
inputfile = sys.argv[1]
outputfile = sys.argv[2]

with open(inputfile, "rt") as f:
	line = f.readline()
	genre = dict()

	while line:
		fline = line.split("::")
		gline = fline[2].split("|")
		gline = list(map(lambda s: s.strip(), gline))
		for i in gline:
			if i not in genre:
				genre[i]=1
			else:
				genre[i]+=1
		line = f.readline()

	keylist = list(genre.keys())
	valuelist = list(genre.values())

	index = 0
	with open(outputfile, "wt") as w:
		for i in genre:
			data = ('{} {}'.format(keylist[index], valuelist[index]))
			index+=1
			w.write(data)
			w.write('\n')
		
	

