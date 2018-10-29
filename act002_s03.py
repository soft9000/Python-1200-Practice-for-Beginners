#!/usr/bin/env python3
# activity: act002_s03.py

def cls(msg=None, zbox = '==='):
    ''' Clear the Lines on the Screen '''
    for ignore in range(50):
        print()
    if zbox is not None:
        print(zbox, "RESTART:", __file__, zbox)
    if msg is not None:
        print(zbox, msg.upper())

cls("act002_s03.py: Function I/P/O Practice")

def zcalc(my_data, opers, trace=False):
    result = 0.0
    for op in opers:
        for fval in my_data:
            expr = str(result) + op +  fval
            result = eval(expr)
            if trace:
                print(expr, "is", result)
    return result
        
# Concept: Testing Series
test_ops = ("+", "*")
test_data = [list("1234554321"),
             ("11.11", "22.22", "33.33", "44.44")]

for test_case, my_data in enumerate(test_data, 1):
        result = zcalc(my_data, test_ops)
        print("Test #", test_case,
              "result is {0:>08.4f}".format(result))
print('...')



