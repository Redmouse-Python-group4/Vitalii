# -*- coding: utf-8 -*-
s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]
words = (s_nouns, p_nouns, s_verbs, p_verbs, infinitives)
mystr = " ".join(choice(word) for word in words)

word = raw_input('Введите слово которое требуется найти и заменить на ревертированное значение: ')
text = re.sub(r'^%s' % word, word[::-1], mystr)
text = re.sub(r'%s$' % word, word[::-1], text)
print text