#!/usr/bin/env python3.6

mylist = []
for letters in 'HELLO':
	mylist.append(letters)
print(mylist)

mydata = [ x ** 2 for x in range(0,11) if x%2 ==0]
print(mydata)

celcius = [0,10,23,14,33]
print(celcius)
far =[ ((9/5) * temp + 32) for temp in celcius]
print(far)
