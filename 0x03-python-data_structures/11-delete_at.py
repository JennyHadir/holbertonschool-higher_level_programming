#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        if idx >= len(my_list) or idx < 0:
            return my_list
        else:
            for rem in my_list:
                if rem - 1 == idx:
                    my_list.remove(rem)
            return my_list
