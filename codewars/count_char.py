"""
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
"""
def count(string):
    count_dict = {}
    if string == "": return count_dict
    for i in string:
        count_dict.update({i : string.count(i)})

    return count_dict

print(count("hello there how are you"))