from collections import namedtuple

cat= namedtuple('Cat','name fur claws')

a=cat(name='Kitty',fur='Fuzzy',claws=False)
print(a)
print("Name of the cat is "+ a.name)
print(a[2])
