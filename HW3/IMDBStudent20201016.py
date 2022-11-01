#!/usr/bin/python3
inputfile = input()
outfile = input()

f = open(inputfile,'r')
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
w = open(outfile,'w')
for i in genre:
	data = ('{} {}'.format(keylist[index], valuelist[index]))
	index+=1
	w.write(data)
	w.write('\n')
	
w.close()
f.close()
