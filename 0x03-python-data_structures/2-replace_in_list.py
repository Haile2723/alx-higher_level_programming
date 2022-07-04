#!/usr/bin/python3
# 2-replace_in_list.py
# Haile2723
def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specified position"""
    if idx <= 0 or idx > len(my_list):
        return (my_list)
    new_element = element
    my_list[idx] = element
    return (my_list)
