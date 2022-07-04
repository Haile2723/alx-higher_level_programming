#!/usr/bin/python3
# 1-element_at.py
# Haile2723

def element_at(my_list, idx):
    """Print an integer at index idx"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (None)
    return (my_list[idx])
