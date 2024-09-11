#!/usr/bin/python3
def uppercase(str):
    for m in str:
        if ord(m) >= 65 and ord(m) <= 90:
            print('{}'.format(True))
        else:
            print ('{}'.format(False))
