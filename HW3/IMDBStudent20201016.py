#!/usr/bin/python3
import sys
f = open('movies.dat','r')
line = f.readline()
while line:
	a = line.split("::")
	print("ID : {}, Title : {}, Genre : {}".format(a[0], a[1], a[2]), end ="")
	line = f.readline()
f.close()
