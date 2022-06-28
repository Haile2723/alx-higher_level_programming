#!/usr/bin/python3
# 12-fizzbuzz.py
# Haile2723
def fizzbuzz():
    for i in range(1, 101):
        print("{} ".format(i), end="")
        if i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        elif i % 15 == 0:
            print("FizzBuzz ", end="")
