#!/usr/bin/python3
# 3-infinite_add.py
# Haile2723


if __name__ == "__main__":
    import sys

    total = 0
    for n in range(len(sys.argv) - 1):
        total += int(sys.argv[n + 1])
    print("{}".format(total))
