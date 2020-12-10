#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            Result = ord(i) - 32
        print("{:c}".format(Result), end = "")
            Result = ord(i)
        print("{:c}".format(Result),end = "")
    print("")
