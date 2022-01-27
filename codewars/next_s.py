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
    """
        - Starting from the right to the left of n:
            - check for a digit x that is larger than the digit that comes just before it (in the loop not the original n).
            - on finding x, traverse through the remaining part of n towards the right end looking for:
                y which will be the NEXT smaller number from x.
                (for example [7,9,4,3,1,8], if x is 9, y will be 8)
            - swap x with y.
            - from the position you found x, + 1, towards the right, sort those numbers in descending order.
            (for example [7,9,4,3,1,8], if x is 9, sort [4,3,1,8])
            - numbers before x remain the same. concat those with this new sorted array.
    """
    #variables:
    n_list = list(str(n))
    reversed_n_list = list(reversed(n_list))
    x = 0
    x_pos = 0
    y = -1
    y_pos = 0
    # edge cases to check for (if n is of len 1, or if digits of n are arranged in ascending order):
    if (len(str(n)) == 1) or (n_list == sorted(n_list)):
        return -1
    # the sorting process
    # step one: check for x and store pos we found x
    for i in range(len(n_list)-1, -1, -1):
        if n_list[i] < n_list[i-1]:
            x = n_list[i-1]
            x_pos = i - 1
            break
    # step two: look for y and store its position
    for i in n_list[x_pos+1:]:
        if int(i) > y and int(i) < int(x):
            y = int(i)
            """
                - getting the y_pos can be tricky if there is more than one occurrence 
                  of a certain digit. This way works.
            """
            initial_y_pos = reversed_n_list.index(str(y))
            y_pos = len(n_list) - initial_y_pos - 1
    # swap x with y
    n_list[y_pos], n_list[x_pos] = n_list[x_pos], n_list[y_pos]
    #step three: sort remaining part of n_list
    remaining = [i for i in n_list[x_pos+1:]]
    sorted_remaining = sorted(remaining, reverse=True)
    ans = "".join([i for i in n_list[0:x_pos+1]] + sorted_remaining)
    # last edge case check: if first value of ans is zero return -1
    if ans[0] == "0":
        return -1
    else:
        return int(ans)

print(next_smaller(3351289442))