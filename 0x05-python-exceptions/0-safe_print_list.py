#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    countIdx = 0
    for i int range(x):
        try:
            print(f"{my_list[i]}", end="")
            countIdx += 1
        except IndexError:
            break
    print()
    return (countIdx)
