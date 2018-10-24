#!/usr/bin/env python3.6
name = "Sunny"
age = 26
bmi=18.4646644666644
#Fomat function 
print("{} is {} years old".format(name,age))

# f-string (formatted string literals) is implemented in 3.6
print(f"{name} is {age} years old")

print("My bmi is {b:1.2f}".format(b=bmi))
