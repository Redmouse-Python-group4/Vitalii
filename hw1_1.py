# -*- coding: utf-8 -*-
 
x=int(raw_input("Введите x "))
if 0<=x<=3:
	str=raw_input("Введите строку ")
	n=int(raw_input("Введите число повтров "))
	for i in range(0, n):
		print str + '\n'
elif 4<=x<=6:
	m=int(raw_input("Введите степень "))
	print "%s в степени %s равно %s"%(x, m, x**m)
elif 7<=x<=9:
	for i in range(0, 10):
		x+=1
		print "%s \n" % x
else:
    print u"Ошибка ввода!\n"