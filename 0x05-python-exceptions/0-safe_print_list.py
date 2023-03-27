#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_pr = 0
    for i int range(x):
        try:
            print(f"{my_list[i]}", end="")
            num_pr += 1
        except IndexError:
            break
    print()
    return (num_pr)
