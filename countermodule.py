#!/usr/bin/env python3.6
from collections import Counter
numbers = [2,4,5,3,4,3,4,3,5,4,7,7,8,4,5]

print(Counter(numbers))


word='lajdfljladfjojjladjfljaldlasdfj'

print(Counter(word))


sentence="How many times the word came in the sentence word is the"

print(Counter(sentence.split()))

c=Counter(sentence.split())
print()
for i in range(80):
	print("-",end='')
print()
print("Most common elements ",c.most_common(2)) # Most common elements
print("Total of all counts ",sum(c.values()))  # Total of all counts
print("List unique element ",list(c))	#List unique elements
print("Convert to a set: ",set(c))	# Convert to a set
print("Convert to dicationary ",dict(c))  # Convert to dictionary
print("Convert to a list of (ele,cnt) pairs ",c.items())


