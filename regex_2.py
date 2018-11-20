#!/usr/bin/env python
import re

def multi_re_find(patterns,phrase):
    for pattern in patterns:
        print("Searching the pattern with : %r" %(pattern))
        print(re.findall(pattern,phrase))
        print("")


phrase="sdds...sd...ss.sdd....sdsdssd..ss.s...."
pattern=[ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

print(phrase)
print("")
multi_re_find(pattern,phrase)
