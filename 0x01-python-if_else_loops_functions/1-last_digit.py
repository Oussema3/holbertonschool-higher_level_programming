#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
    s = number % 10
    number = -number
    s = -s

else:
    s = number % 10
if s > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, s))
elif s == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, s))

else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, s))
