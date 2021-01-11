#!/usr/bin/python3
""" Queen moves in chess """
from sys import argv
if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
        N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)
    move = []
    for i in range(N):
        move.append([i, None])
