#!/usr/bin/python3
# 10-divisible_by_2.py
# Haile2723


def divisible_by_2(my_list=[]):

    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(true)
        else:
            multiples.append(false)
    return (multiples)
