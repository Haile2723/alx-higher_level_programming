#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lt_digit = abs(number) % 10
if number < 0:
    lt_digit = -lt_digit
    print("Last digit of {} is {} and is ".format(number, lt_digit), end="")
    if lt_digit > 5:
        print("greater than 5")
    elif lt_digit == 0:
        print("0")
    else:
        print("less than 6 and not 0")
