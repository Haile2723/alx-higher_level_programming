#!/usr/bin/python3
# 2-replace_in_list.py
# Haile2723


def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specified position"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
