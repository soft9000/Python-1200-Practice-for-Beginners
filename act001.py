#!/usr/bin/env python3
# activity: act001.py

def cls():
    ''' Clear the Lines on the Screen '''
    for ignore in range(100):
        print()

my_str = "Welcome to act001.py"

cls()
print("type(",type(my_str),") Value:", my_str)

print("len(",len(my_str),")")

for ch in my_str:
    print("char:", ch, "ord(", ord(ch), ")")
    
for ich in range(9818, 9828):
    print(chr(ich), end='')

    
