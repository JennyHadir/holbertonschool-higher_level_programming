#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) is float:
        div = int(div)
    if type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError ("matrix must be a matrix (list of lists) of integers/float")
    for under in matrix:
        for i in under:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/float")
