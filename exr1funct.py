#!/usr/bin/env python

def lessorgreat(a,b):
	if a%2 == 0 and b%2 == 0:
		return min(a,b)
	else:
		return max(a,b)
print(lessorgreat(2,4))
print(lessorgreat(5,2))
