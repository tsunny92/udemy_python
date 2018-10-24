#!/usr/bin/env pythoon3.6

'''
Here args demo has been shown, all args are taken in set  
'''
def calaverage(*args):
	print(args)
	return (sum(args)/len(args))
print(calaverage(10,20,30,39,44))

'''
Keyword args (kwargs) has been shown , all args are taken in dictionary format
'''

def kwargsdemo(**kwargs):
	print(kwargs)
	if 'fruit' in kwargs:
		print("My fav fruit is ", kwargs['fruit'])
	else:
		print("No fruit found")
kwargsdemo(veggie='Potato',fruit='Apple')	
