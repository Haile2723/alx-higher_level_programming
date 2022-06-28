#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lt_digit = abs(number) % 10
if lt_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lt_digit, end=" "))
elif lt_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, lt_digit, end=" "))
elif lt_digit < 6 and lt_digit > 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lt_digit, end=" "))
