# a function that returns the sum of two lowes numbers in an array
def array_check(arr):
    summation = sorted(arr)[0] + sorted(arr)[1]
    print(summation)

    
array_check([21, 5, 59, 2])