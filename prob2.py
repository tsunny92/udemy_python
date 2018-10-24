#!/usr/bin/env python
def sntce(word):
	str1 = word.split()
	return ' '.join(str1[::-1])

print(sntce('Hello World'))
