# -*- coding: utf-8 -*-
 
print u"Общество в начале XXI века"
age=int(raw_input("Введите ваш возраст "))
if 0<=age<=7:
    print u"Вам в детский сад"
elif age<=18:
    print u"Вам в школу"
elif age<=25:
    print u"Вам в профессиональное учебное заведение"
elif age<=60:
    print u"Вам на работу"
elif age<=120:
    print u"Вам предоставляется выбор"
else:
    error = u"Ошибка! Это программа для людей!\n"
    print error*5