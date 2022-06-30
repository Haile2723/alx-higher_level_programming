#!/usr/bin/python3
# 1-calculation.py
# Haile2723


if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add()))
    print("{} - {} = {}".format(a, b, sub()))
    print("{} * {} = {}".format(a, b, mul()))
    print("{} / {} = {}".format(a, b, div()))
