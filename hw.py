# -*- coding: utf-8 -*-

from random import choice
from string import lowercase

s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]
words = (s_nouns, p_nouns, s_verbs, p_verbs, infinitives)
string_val = " ".join(choice(word) for word in words)
# string_val = " ".join(choice(lowercase) for i in range(10))
biges_str = ""
print string_val+'\n'

for word in string_val.split():
	if len(biges_str)<len(word):
            biges_str= word
print u"Саммая длинная строка - %s %s символов"%(biges_str, len(biges_str))

string_val = ";".join(choice(lowercase) for i in range(10))
for word in string_val.split(';'):
	if len(biges_str)<len(word):
            biges_str= word
print u"Саммая длинная строка - %s %s символов"%(biges_str, len(biges_str))

string_val = raw_input("Введите строку ")
string_list=string_val.split()
if len(string_list)>0:
	small_word = string_list[0]
	for word in string_val.split():
		if len(small_word)>len(word):
		    small_word= word
	print u"Саммая короткая строка - %s %s символов" % (small_word, len(small_word))
else:
	print u"Нет слов в строке"

string_val = raw_input("Введите строку ")
string_find = raw_input("Введите слово для поиска ")

if string_find in string_val:
	position = string_val.find(string_find)
	print u"'%s%s%s' номер позиции %s"%(string_val[:position], string_find.upper(), string_val[position+len(string_find):], position)
 	
string_val = raw_input("Введите строку ")
print u"Слов в строке '%s' ровно %s"%(string_val, len(string_val.split()))
