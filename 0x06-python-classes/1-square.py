#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self._size = size


my_square = Square(1)
try:
    print(my_square._size)
except TypeError:
    return(None)
