#!/usr/bin/python3
from openpyxl import Workbook
import math

wb = Workbook()

ws = wb.active

row_max = ws.max_row

total=[]
for t in range(2, row_max+1):
	#total
	midtern = ws.cell(row = t, column = 3).value * 0.3
	final = ws.cell(row = t, column = 4).value * 0.35
	homework = ws.cell(row = t, column = 5).value * 0.34
	attendance = ws.cell(row = t, column = 6).value * 100 * 0.01
	total_value = midtern + final + homework + attendance
	total.append(total_value)
	ws.cell(row = t, column = 7, value = total_value)

total.sort(reverse=True)
dic = []

for i in range(len(total)):
	dic.append('Z')
	
Agrade = math.trunc(len(total)*0.3)
Bgrade = math.trunc(len(total)*0.7)

for index in range(len(total)):
	if(index < Agrade):
		dic[index] = 'A0'
		for i in range(len(total)):
			if(total[index] == total[i]):
				dic[i] = dic[index]
	elif(index < Bgrade):
		dic[index] = 'B0'
		for i in range(len(total)):
			if(total[index] == total[i]):
				dic[i] = dic[index]
	else:
		dic[index] = 'C0'
		for i in range(len(total)):
			if(total[index] == total[i]):
				dic[i] = dic[index]
Acount=0
Bcount=0
Ccount=0
for index in range(len(total)):
	if(dic[index] == 'A0'):
		Acount+=1
	if(dic[index] == 'B0'):
		Bcount+=1
	if(dic[index] == 'C0'):
		Ccount+=1
A_count = Acount//2
B_count = Bcount//2
C_count = Ccount//2

for index in range(0,A_count):
	dic[index] = 'A+'
	
for index in range(Acount,Acount+B_count):
	dic[index] = 'B+'
	
for index in range(Acount+Bcount,Acount+Bcount+C_count):
	dic[index] = 'C+'
	
for g in range(2, row_max+1):
	count = -1
	for t in total:
		count+=1	
		if(ws.cell(row = g, column = 7).value == t):
			ws.cell(row = g, column = 8, value = dic[count])
	
wb.save("student.xlsx")
