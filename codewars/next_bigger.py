"""
Create a function that takes a positive integer and returns the next bigger number
that can be formed by rearranging its digits.
For example:
    12 ==> 21
    513 ==> 531
    2017 ==> 2071
    nextBigger(num: 12)   // returns 21
    nextBigger(num: 513)  // returns 531
    nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):
    9 ==> -1
    111 ==> -1
    531 ==> -1
    nextBigger(num: 9)   // returns nil
    nextBigger(num: 111) // returns nil
    nextBigger(num: 531) // returns nil
"""

def next_bigger(n):
    """
        - Algorithm to solve this
        - Traverse through a n from the right to the left checking for:
            - a digit b which is smaller than the digit just before it (in the loop during traversing, not in original n)
            (for example, if n_list = [4,3,6,5,9,8,7] b is 5) and store its position in some variable.
        - on finding b, traverse through n starting from one position after where b was found towards the right:
            - check for a number z, which is the NEXT larger number from b.
            (for example in n_list = [4,3,6,5,9,8,7] z is 7) and store its position in another variable.
        - Swap b and z in n.
        - After the swap, sort in ascending order numbers, from position b + 1 to the right end.
        - numbers to the left of b remain the same. concat those with this new sorted array.
    """
    #variables:
    n_list = list(str(n))
    reversed_n_list = list(reversed(n_list))
    b = 0
    b_pos = 0
    z = 1000000000000000000000
    z_pos = 0
    # edge cases: (if len of n is 1, or n digits are arranged in descending order)
    if len(str(n)) == 1 or (n_list == sorted(n_list, reverse=True)):
        return -1
    # The sorting process
    # step 1: get b and store its position
    for i in range(len(n_list)-1, -1, -1):
        if n_list[i-1] < n_list[i]:
            b = n_list[i-1]
            b_pos = i - 1
            break
    # step 2: get z and store its position
    for i in n_list[b_pos+1:]:
        if int(i) > int(b) and int(i) < z:
            z = int(i)
            """
             - getting the z_pos can be tricky if there is more than one occurrence 
               of a certain digit. This way works.
            """
            initial_z_pos = reversed_n_list.index(str(z))
            z_pos = len(n_list) - initial_z_pos - 1
    # step 3: swap b and z
    n_list[b_pos], n_list[z_pos] = n_list[z_pos], n_list[b_pos]
    # step 4 : sort numbers to the right of b
    remaining = [i for i in n_list[b_pos+1:]]
    sorted_remaining = sorted(remaining)
    # last step: concat
    ans = "".join(n_list[0:b_pos+1] + sorted_remaining)
    if ans[0] != "0":
        return int(ans)
    else:
        return -1


print(next_bigger(3318262064))  # should equal 3318262406
print(next_bigger(573852))  # should equal 575238