#!/usr/bin/env python3
# activity: fcls.py

def cls():
    ''' Clear the Lines on the Screen '''
    for ignore in range(100):
        print()

def fcls():
    ''' Clear the screen, and displays full file name '''
    cls()
    zbox = '=' * 3
    print(zbox, "RESTART:", __file__, zbox)


fcls()
