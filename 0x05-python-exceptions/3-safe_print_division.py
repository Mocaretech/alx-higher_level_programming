#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b

        print("Inside result: {}".format(result))
    except(ZeroDivisionError, TypeError):
        result = None
        print("Inside result: None")

    finally:
    return result
