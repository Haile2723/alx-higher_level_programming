#!/usr/bin/python3
# 8-multiplr_returns.py
# Haile2723


def multiple_returns(sentence):

    if len(sentence) == 0:

        sentence[0] = None

    length = len(sentence)
    first = sentence[0]

    return (length, first)
