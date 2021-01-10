#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new = []
        for i in my_list:
            if i != my_list[idx]:
                new.append(i)
        return new 
