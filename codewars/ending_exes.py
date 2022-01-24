"""remove exclamation marks from the end of the string...only those at the end"""
# without using rstrip method

def remove(s):
    x = s[::-1]
    idx = 0
    z = s[::-1]
    while x[idx] == "!":
        z = x[idx+1:]
        idx += 1
    return z[::-1]

"""
    while s and s[-1] == "!":
        s = s[:-1]
"""


print(remove("!Hi"))