"""
You will be given an array of numbers.
You have to sort the odd numbers in ascending order
while leaving the even numbers at their original positions.
"""

def sort_array(source_arr):
    #first get a dictionary out of the array
    dict_form = dict(enumerate(source_arr))

    x = []

    #store all the odd numbers in x
    for i in source_arr:
        if i % 2 != 0:
            x.append(i)

    #sort the odd numbers list so as to be replaced in order
    ordered_x = sorted(x)

    """
    loop through the dict replacing any value that is odd with 
    the first item of the x array, and remove that value from x
    after that 
    """
    for k, v in dict_form.items():
        if v % 2 != 0:
            dict_form[k] = ordered_x[0]
            ordered_x.remove(ordered_x[0])

    #convert the dict back to an array
    final_arr = [value for value in dict_form.values()]
    return final_arr

sort_array([5, 8, 6, 3, 4])