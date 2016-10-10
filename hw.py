# -*- coding: utf-8 -*-
import csv
import json

def count_result(my_array):
	result = dict()
	for i in my_array: 
		if i['metrick'] in result:
			result[i['metrick']]+=1
		else:
			result[i['metrick']]=1
	return result

f = open ("price.txt","r")
pricelist = list()
for line in f:
     row = line.split()
     pricelist.append({'name': row[0], 'count': row[1], 'metrick': row[2]})  
f.close()
result = count_result(pricelist)

f = open("price.txt","a")
for key, value in result.iteritems():
	f.writelines("\nКолличество %s: %s"%(key, value))
f.close()

f_s = open("price.csv","r")
pricelist = list()
f = csv.reader(f_s)
for row in f:
	pricelist.append({'name': row[0], 'count': row[1], 'metrick': row[2]})
f_s.close()
result = count_result(pricelist)

f_s = open("price.csv","a")
f = csv.writer(f_s, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for key, value in result.iteritems():
	f.writerow(["Колличество", key, value])
f_s.close()

f_s = open("price.json")
pricelist = list()
f = json.load(f_s)
for row in f:
	pricelist.append({'name': row['name'], 'count': row['count'], 'metrick': row['metrick']})
f_s.close()
result = count_result(pricelist)

f_s=open("result.json", "wb")
json.dump(result, f_s)
f_s.close()