#!/usr/bin/python3
def multiple_returns(sentence):
    re = None
    size = len(sentence)
    if size > 0:
        re = sentence[0]
    return size, re
