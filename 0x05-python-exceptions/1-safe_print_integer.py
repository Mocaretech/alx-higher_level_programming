#!/usr/bin/python3
def safe_print_integer(value):
    value = input("please enter the value")
    try:
        print("{:d}".format(value))
        return(True)
    except (ValueError, TypeError:)
        print("Opp, this is not an integer")
        return(False)
