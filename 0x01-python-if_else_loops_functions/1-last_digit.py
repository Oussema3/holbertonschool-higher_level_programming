#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
f = "Last digit of"
if number < 0:
    number = -number
    s = number % 10
    s = -s

else:
    s = number % 10
if s > 5:
    print(f, number, "is", s, "and is greater then 5")
elif s == 0:
    print(f, number, "is", s, "and is 0")
else:
    print(f, number, "is", s, "and is less than 6 and not 0")
