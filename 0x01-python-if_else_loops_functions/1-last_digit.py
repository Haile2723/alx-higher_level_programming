#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = (abs(number)) % 10
if x > 0:
    print("Last digit of {} is {} ".format(number, x), end="")
    if x > 5:
        print("and is greater than 5")
    elif x == 0:
        print("and is 0")
    else:
        if number < 0:
            x = -x
        print("and is less than 6 and not 0")
