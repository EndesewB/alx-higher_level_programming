#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d} is an integer".format(value))
        return True
    except ValueError:
        return False
