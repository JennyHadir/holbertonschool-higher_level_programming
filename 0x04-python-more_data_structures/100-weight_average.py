#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        weight = 0
        score = 0
        for i in my_list:
            score += i[1]
            weight += i[0] * i[1]
        return weight / score
    return 0
