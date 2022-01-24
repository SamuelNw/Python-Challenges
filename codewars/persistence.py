"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.
"""
from functools import reduce

def persistence(num):
    """
        n = 0
        if len(str(num)) == 1:
            return 0
        product = 1
        while len(str(num)) > 1:
            for item in str(num):
                product = product * int(item)
            num = product
            n += 1
            product = 1
        return n
    """
    #optimization of the same function
    x = 0
    lis = list(str(num))
    while len(lis) > 1:
        product = reduce(lambda a, b: int(a)*int(b), lis)
        lis = list(str(product))
        x += 1
    return x

print(persistence(39865211455))