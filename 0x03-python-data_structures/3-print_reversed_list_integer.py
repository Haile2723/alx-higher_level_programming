#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Haile2723

def print_reversed_list_integer(my_list=[]):
    """Print an integer in reverse order"""
    for i in range(len(my_list)):
        print("{:d}".format(reverse(my_list[i])))
