#!/usr/bin/python3
# 7-add_tuple.py
# Haile2723

def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2:
        for i in tuple_a:
            if tuple_a[i] == NULL:
                tuple_a[i] = 0
    else:
        tuple_a = tuple_a[0], tuple_a[1]
    if len(tuple_b) < 2:
        for i in tuple_b:
            if tuple_b[i] == NULL:
                tuple_b[i] == 0
    else:
        tuple_b = tuple_b[0], tuple_b[1]

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
