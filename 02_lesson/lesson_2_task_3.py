import math


def square(arg):
    return math.ceil(arg * arg)


arg = float(input())
result = square(arg)
print(result)
