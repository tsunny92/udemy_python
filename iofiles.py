#!/usr/bin/env python3.6
#with open('testing.txt','a') as testingfile:
#	testingfile.write('\nGo for it')

#with open('testing.txt') as testingfile:
#        contents = testingfile.read()
#print(contents)

with open('testing.txt','w+') as testingfile:
        testingfile.write('Hello testing files')
	contents = testingfile.read()
print(contents)
