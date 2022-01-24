"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""
import functools


def zeros(n):
    """
        Each multiple of 5 adds a 0, so first we count how many multiples of 5 are
        smaller than `n` (`n // 5`).

        Each multiple of 25 adds two 0's, so next we add another 0 for each multiple
        of 25 smaller than n.

        We continue on for all powers of 5 smaller than (or equal to) n.
        """
    pow_of_5 = 5
    zeros = 0

    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5

    return zeros



print(zeros(100))
