#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        c = chr(i - 32)
        print("{:s}".format(c), end = "")
    else:
        c = chr(i)
        print("{:s}".format(c), end = "")
