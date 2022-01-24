"""
Given an n x n array, return the array elements arranged from outermost
elements to the middle element, traveling clockwise.
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
"""

array = [1,1,2,1,2,5,5,4]

array1 = [[1,2],
         [3,4]]

array2 = [[1,2,3,10],
         [8,9,4,11],
         [7,6,5,12],
         [13,14,15,16]]

array3 = [[1,2,3],
         [8,9,4],
         [7,6,5]]

array4 = [[1,2,3,10,20],
         [8,9,4,11,21],
         [7,6,5,12,22],
         [13,14,15,16,23],
            [8,9,4,11,21],]

array5 = [[1,2,3,10,20,56],
         [8,9,4,11,21,36],
         [7,6,5,12,22,39],
         [13,14,15,16,23,41],
            [8,9,4,11,21,59],
          [25,68,87,79,54,40]]

def snail(snail_map):
    # declare an empty array for the answer
    ans = []
    # if the array is a 1d, return it
    if type(snail_map[0]) == int:
        ans = snail_map
        return ans
    # check for the number of sub arrays in the array given and store in a variable
    main_array_length = len(snail_map[0])
    # if array is a 2 * 2, just append to ans first arr in order, and second in reversed order
    if main_array_length == 2:
        for val in snail_map[0]:
            ans.append(val)
        for val in snail_map[1][::-1]:
            ans.append(val)
        return ans
    # for any other array larger than a 2*2
    # create a big while loop dependent on the length of the snail_map --> stops looping while the arr is empty
    while len(snail_map) > 0:
        # append values of the first sub array in order to the ans, and pop that sub array from the main array.
        for val in snail_map[0]:
            ans.append(val)
        snail_map.pop(0)
        #this condition checks if after popping that first array, the main array remains empty
        if len(snail_map) == 0:
            return ans
        # move unto the next sub array, if it is not the last of the main array, pop the last val and append to ans
        # repeat till you get to the last array, after which you will append its values in reverse order into ans, then pop
            # it from the original array.
        num_of_arrays_remaining = 1
        idx_to_check = 0
        while len(snail_map) > num_of_arrays_remaining:
            ans.append(snail_map[idx_to_check].pop(-1))
            idx_to_check += 1
            num_of_arrays_remaining += 1
            continue
        for val in snail_map[-1][::-1]:
            ans.append(val)
        snail_map.pop(-1)
        # start from the current last sub array, if it is not the only one remaining, pop and append the first value
            # into ans,
        # then move to the second last sub array and repeat the check and process,
        # if it is the last array, append values in order into ans then pop it from the main array
        num_of_arrays_remaining_2 = 1
        idx_to_check_2 = -1
        while len(snail_map) > num_of_arrays_remaining_2:
            ans.append(snail_map[idx_to_check_2].pop(0))
            idx_to_check_2 -= 1
            num_of_arrays_remaining_2 += 1
            continue
        continue
    return ans


print(snail(array4))
