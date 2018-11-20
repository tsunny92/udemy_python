#!/usr/bin/env python

import re

words = ['Hello','world']

sentence = "Hello Everyone"

match = re.search(words[0], sentence)
print(match.start())

for word in words:
    if re.search(word, sentence):
        print("Match found")
    else:
	print("No match found")


emails = ['hello@ymail.com', 'kill@gmal.com', 'abc@xyz.com', 'sunny@endurance.com']

for domain in emails:
    print("User name is "+re.split('@',domain)[0])
    print("Domain name is "+re.split('@',domain)[1])


# Returns a list of all matches
print(re.findall('hello','hello my name is hello'))


