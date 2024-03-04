#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique1 = []
    for x in my_list:
        if x not in unique1:
            unique1.append(x)
    total = sum(unique1)
    return total

