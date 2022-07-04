#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Haile2723

def print_reversed_list_integer(my_list=[]):
    """Print an integer in reverse order"""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
