#!/usr/bin/env python3.6

def add_fun(n1=1,n2=3):
	return n1 + n2
'''
Default value 
'''
print(add_fun())
print(add_fun(10,20))

def check_dog(mystring):
	return 'dog' in mystring.lower()
print(check_dog('Dog ran away'))

def piglatin(word):
	fl = word[0].lower()
	if fl in 'aeiou':
		word = word + 'ay'
	else:
		word = word[1:] + fl + 'ay'
	return word
print(piglatin('Word')) 
