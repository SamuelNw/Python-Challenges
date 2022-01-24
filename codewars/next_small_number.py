"""
    Write a function that takes a positive integer and returns the next smaller
    positive integer containing the same digits.
    For example:
    next_smaller(21) == 12
    next_smaller(531) == 513
    next_smaller(2071) == 2017
    Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that
    contains the same digits.
    Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.
    next_smaller(9) == -1
    next_smaller(135) == -1
    next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
"""

def next_smaller(n):
    ans = -1
    ans_2 = ""
    #if n is smaller than 10 (is a one digit num) return -1
    if n < 10 or n == 123456789: return ans
    # optimization tip to try, ans must have same length as n, so from list range(10, n) filter all those nums
    # with less digits than n.
    n_length = len(str(n))
    """
        looping through the list of numbers from n-1 towards 10, with the length of n in mind: 
            - for each number in that list:
                - first store its length somewhere - num_length
                - store another value x = total number of chars in num present in n
                - looping through the individual chars for n, for each char present in num increment x by 1
                - after looping through all, if x = num_length, num is our answer.
    """
    y = list(str(n))
    while n_length == len(str(n-1)):
        x = n - 1
        z = list(str(x))
        total_len = 0
        for i in y:
            if i in z:
                total_len += 1
                z.remove(i)
        if total_len == n_length:
            ans_2 = x
            break
        else:
            n = x
            ans_2 = ans
    return ans_2



print(next_smaller(5221559965523))

#as much as this works, it is slower than required. check for the correct soln in the next_s.py file