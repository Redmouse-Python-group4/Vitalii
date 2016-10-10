# -*- coding: utf-8 -*-

import random
choice = ["Да","Нет", "Не знаю", "Выбор очевиден!","Бог знает", "Тупой вопрос", "Хмм...","Да ну на ?!","Так точно !"]
while True:
	question = raw_input('Задайте Ваш вопрос: ')
	print "%s - %s"%(question, random.choice(choice))
	exit = raw_input('Еще раз (Y/N)? ')
	if exit == 'N' or exit=='n':
		break
