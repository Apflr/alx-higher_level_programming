#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx <= 0:
        return my_list.copy()
    elif idx >= len(my_list):
        return my_list.copy()
    else:
        newer = my_list.copy()
        newer[idx] = element
        return newer
