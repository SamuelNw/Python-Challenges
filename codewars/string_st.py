""":cvar
This is a spin off of my first kata. You are given a list of character sequences as a comma separated string.
Write a function which returns another string containing all the character sequences except the first and
 the last ones, separated by spaces.
If the input string is empty, or the removal of the first and last items
would cause the string to be empty, return a null value.
"""

def st_check(string):
    if len(string.split(",")) < 3:
        return None
    else:
        return " ".join(string.split(",")[1:-1])


print(st_check("1,2,3,5"))
