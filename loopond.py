#!/usr/bin/env python

x = [1,2,3]

for items in x:
	pass
print("Does nothing using pass")

str1 = "Rahul"
for letter in str1:
	if letter == 'h':
		continue	
	print(letter)
	if letter == 'u':
		break
