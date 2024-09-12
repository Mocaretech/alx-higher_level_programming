#!/usr/bin/python3
def uppercase(str):
    for m in str:
        if 97 <= ord(m) and ord(m) <=122:
            alphabt = chr(ord(m) - 32)
            print('{}'.format(alphabt), end="")
        print()
