"""
Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas except for the last two names,
which should be separated by an ampersand.
"""
def namelist(names):
    arr = []
    for item in names:
        for value in item.values():
            arr.append(value)
    if len(arr) == 0: return ""
    if len(arr) == 1:
        return "".join([name for name in arr])
    else:
        y = arr.pop()
        x = ", ".join([name for name in arr])
        x += f" & {y}"

    return x

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))