#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 98 and ord(i) < 123:

            Result = ord(i) - 32
           
        else:
            Result = ord(i)
        print("{:c}".format(Result),end="")
    print("")
