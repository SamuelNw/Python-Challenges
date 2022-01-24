"""
Move all exclamation marks to the end of the sentence
"""

def remove(s):
    q = s.replace("!", "")
    return q + ("!" * s.count("!"))


print(remove("Hi! Hi! hi!"))