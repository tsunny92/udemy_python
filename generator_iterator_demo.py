#!/usr/bin/env python3.6

def simple_gen():
	for x in range(3):
		yield x	

for no in simple_gen():
	print(no)

g = simple_gen()
print("------------")
print(next(g))
print(next(g))

n = simple_gen()
s_iter=iter(n)

print("------------")
print(next(s_iter)," ",next(iter(s_iter))," ", next(iter(s_iter)))
