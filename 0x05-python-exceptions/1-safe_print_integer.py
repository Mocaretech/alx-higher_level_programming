#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return(True)
    except (ValueError, TypeError):
        return(False)
    Exception as glitch:
        print("This is not a valid")
        return (False)
