#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except(ZeroDivisionError, TypeError):
        result = None
    finally:
        print("{:d} / {:d} = inside result: {}".format(a, b, result))
    return(result)
