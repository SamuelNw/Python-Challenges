"""
Define a function that takes one integer argument and returns
logical value true or false depending on if the integer is a prime.
"""
from math import sqrt

def is_prime(num):
    #first check for any numbers less than 2, are 2 or are even
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    """
        Property:
            Every number n that is not prime has at least one prime divisor p
            such 1 < p < square_root(n).
            as a result, we don't need to loop through all numbers through to our number n
    """
    root = int(sqrt(num))
    #to improve performance even further, we loop through only the odd numbers
    for i in range(3, root+1, 2):
        if num % i == 0:
            return False
    return True

print(is_prime(17))
