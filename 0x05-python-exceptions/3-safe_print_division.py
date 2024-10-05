#!/usr/bin/python3
def safe_print_division(a, b):
    result = a / b
    try:
        print("Inside result: {:d}".format(result))
    except(ZeroDivisionError, TypeError):
        return(None)
    finally:
        print("{:d} / {:d} = {:d}".format(a, b, result))
    return(result)
