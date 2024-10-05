#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("{:d} / {:d} = inside result: {}".format(a, b, result))
    except(ZeroDivisionError, TypeError):
        return(None)
    finally:
        print("{:d} / {:d} = {:d}".format(a, b, result)
    return(result)
