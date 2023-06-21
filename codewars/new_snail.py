"""
Given an n x n array, return the array elements arranged from outermost
elements to the middle element, traveling clockwise.
array = [[1,2,3],
        [4,5,6],
        [7,8,9]]
spiral(array) #=> [1,2,3,6,9,8,7,4,5]
"""

array = [1, 1, 2, 1, 2, 5, 5, 4]

array1 = [[1, 2],
          [3, 4]]

array2 = [[1, 2, 3, 10],
          [8, 9, 4, 11],
          [7, 6, 5, 12],
          [13, 14, 15, 16]]

array3 = [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]]

array4 = [[1, 2, 3, 10, 20],
          [8, 9, 4, 11, 21],
          [7, 6, 5, 12, 22],
          [13, 14, 15, 16, 23],
          [8, 9, 4, 11, 21],]

array5 = [[1, 2, 3, 10, 20, 56],
          [8, 9, 4, 11, 21, 36],
          [7, 6, 5, 12, 22, 39],
          [13, 14, 15, 16, 23, 41],
          [8, 9, 4, 11, 21, 59],
          [25, 68, 87, 79, 54, 40]]


def spiral(matrix: list) -> list:
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []

    while left < right and top < bottom:
        # get every i from the top row:
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        # get every i from the right column:
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        # do a check
        if not (left < right and top < bottom):
            break

        # get every i from the bottom row backwards:
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        # get every i from the left column backwards:
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        # increment left
        left += 1

    return res


# prints-> [1, 2, 3, 10, 20, 21, 22, 23, 21, 11, 4, 9, 8, 13, 7, 8, 9, 4, 11, 12, 16, 15, 14, 6, 5]
print(spiral(array4))
