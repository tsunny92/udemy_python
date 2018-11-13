
from collections import defaultdict

d = {'name':'Sunny'}
print(d)
d = defaultdict(object)
print(d['one'])
for i in d:
	print i

d = defaultdict(lambda : 0)

print(d['one'])
d['two'] = 2
print(d['two'])

print(d) 
