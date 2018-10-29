#!/usr/bin/env python3
# activity: checkers.py

def cls():
    ''' Clear the Lines on the Screen '''
    for ignore in range(100):
        print()

def draw_cell(token):
    return "[" + token + "]"
    
cls()

checker_white = chr(0x26c0)
checker_black = chr(0x26c2)
free_space = chr(0x2610)

for row in range(9):
    sep = '  ' + draw_cell(chr(0x245f + row)) + ' '
    if row is 0:
        print(' ' * 8, end='')
        for char in range(ord('ⓐ'), ord('ⓘ')):
           print(draw_cell(chr(char)), end='')
        print("\n")
    elif row is 1 or row is 2:
        print(sep, draw_cell(checker_black) * 8)
    elif row is 7 or row is 8:
        print(sep, draw_cell(checker_white) * 8)
    else:
        print(sep, draw_cell(free_space) * 8)

