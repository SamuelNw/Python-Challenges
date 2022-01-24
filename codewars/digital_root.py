"""
Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.
"""

def digital_root(number):
    if len(str(number)) < 2:
        print(number)
    else:
        while len(str(number)) > 1:
            summation = (sum([int(i) for i in str(number)]))
            number = summation
        print(number)
digital_root(493193)