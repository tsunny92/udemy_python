#!/usr/bin/env python
def myfunc(word):
    word1=''
    for num in range(len(word)):
        j = word[num]
        if num==0 or num==3:
            j = word[num].upper()
        word1 += j
    return word1

print(myfunc('macdonald'))


def same(word):
	if len(word) > 3:
		return word[:3].capitalize() + word[3:].capitalize()

		# For first and last letters
		#return word[:len(word)-1].capitalize() + word[len(word)-1:].capitalize()

	else:
		print("Name is too short")


print(same('macdonald'))
