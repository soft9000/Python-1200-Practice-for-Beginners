#!/usr/bin/env python3
# activity: act002.py

def cls(msg=None, zbox = '==='):
    ''' Clear the Lines on the Screen '''
    for ignore in range(50):
        print()
    if zbox is not None:
        print(zbox, "RESTART:", __file__, zbox)
    if msg is not None:
        print(zbox, msg.upper())

cls("Welcome to act002.py: Function & Formatting Practice")

# Classic Formatting
dum = "%08.04f" % 12.2
print(dum)

# FString Formatting
dum = "{0:08.04f}".format(12.2)
print(dum)

# Justification
print("%+20s" % "Eggs")
print("{0:~<20s}".format("Eggs"))

# Data Series
my_str = "1234554321"
print(tuple(my_str))
print(list(my_str))
print(set(my_str))

# Data Processing & Type Conversion
# (String, Int, Float)
value = 0
for char in tuple(my_str):
    value += float(int(char) * 10.1)
    print("$ {0:>08.4f}".format(value))

# Activity: Stringified Math Operations
print('\n\n\n')
my_data = ("11.11", "22.22", "33.33", "44.44")
opers = ("+", "-", "*", "/")
for op in opers:
    value = 100.0
    for fval in my_data:
        value = eval(str(value) + op +  fval)
        print(op, "$ {0:>08.4f}".format(value))
    print('...')



