#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quetion = a / b
    except (ZeroDivisionError, ValueError):
        quetion = None
    finally:
        print("Inside result: {}".format(quetion))
    print()
    return (quetion)
