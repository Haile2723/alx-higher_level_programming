#!/usr/bin/python3
# 4-new_in_list.py
# Haile2723


def new_in_list(my_list, idx, element):
    """Replace an element in list at specific position."""
    if idx < 0 or idx > len(my_list):
        return (copy(my_list))
    my_list[idx] = element
    return (my_list)

