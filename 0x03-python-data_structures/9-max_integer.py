#!/usr/bin/python3
# 9-max_integer.py
# Haile2723



def max_integer(my_list=[]):

    if len(my_lis) == 0:
        return (None)
    

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return (big)
