#!/usr/bin/python3
def __init__(self, size=0):
    self._size = size
    if not isinstance(size, int):
        raise TypeError:
            print("size must be an integer")
    if size < 0:
        raise ValueError:
            print("size must be >= 0")
