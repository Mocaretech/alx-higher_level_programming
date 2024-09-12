#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print('0 argument:')
    elif arg_count == 1:
        print('1 argument:')
    else:
        print(f"{arg_count} argument")
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[1]}")

