#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return(my_list)
    new_list = my_list[:]
    new_liist[idx] = element
    for elemnt in new_list:
        print(elemnt)
    return(new_list)
