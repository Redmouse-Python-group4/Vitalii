# -*- coding: utf-8 -*-

from hw import hw1_1

x=int(raw_input("Введите x "))
if 0<=x<=3:	
	print hw1_1.func1_3(x)
elif 4<=x<=6:
	print hw1_1.func4_6(x)
elif 7<=x<=9:
	print hw1_1.func7_9(x)
else:
    print u"Ошибка ввода!\n"