#!/usr/bin/python3
# 0-safe_print_list.py
# Haile2723

def safe_print_list(my_list=[], x=0):
    """Print x element of a list

    Args:
        my_list (list): The list to print element from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range (x):
        try:
            print("{}".format(my_list[i]), end="")
            ret +=1
        except IndexError:
            break
    print("")
    return (ret)
