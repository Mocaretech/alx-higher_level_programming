#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except(ZeroDivisionError, TypeError):
        result = None
    finally:
    print("{} / {} = {}".format(a, b, result))
