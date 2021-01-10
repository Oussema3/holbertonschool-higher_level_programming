#!/usr/bin/env python3
def no_c(my_string):
    void = ""
    for i in my_string:
        if i != "c" and i != "C":
            void = void + i
    return void
