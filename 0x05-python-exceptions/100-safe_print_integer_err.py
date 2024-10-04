#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as glitch:
        print("Exception {}".format(glitch), file = sys.stderr)
        return (False)


