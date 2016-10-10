# -*- coding: utf-8 -*-

import os, time

def get_info(path):
	result = list()
	if os.path.exists(path):
		result.append(u"Размер %s"%os.path.getsize(path))
		result.append(u"Дата создания %s"%time.ctime(os.path.getmtime(path)))
		result.append(u"Путь %s"%os.path.abspath(path))
		if os.path.isdir(path):
			result.append(u"Это директория")
		else:
			result.append(u"Это файл")
		
	else:
		result.append(u"Что то ничего не нашел по этому пути %s"%path)
	return result


path = raw_input("Введите путь ")
fname = raw_input("Введите название файла/папки ")

full_name=os.path.join(path, fname)

print "\n".join(get_info(full_name))
