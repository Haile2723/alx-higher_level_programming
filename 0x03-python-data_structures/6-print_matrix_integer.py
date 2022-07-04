#!/usr/bin/python3
# 6-print_matrix_integer.py
# Haile2723



def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integer"""

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i] - 1):
                    print(" ", end="")

        print("")
