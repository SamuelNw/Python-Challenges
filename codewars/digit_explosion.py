"""Given a string made of digits [0-9],
return a string where each digit is repeated a number of times equals to its value."""

def explode(string):
    ans = ""
    for i in list(string):
        ans += i * int(i)
    return ans


print(explode("325"))