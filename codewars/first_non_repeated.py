"""
Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter. For example,
the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
"""
def first_non_repeated_letter(string):
    repeated_letter = ""
    for char in string:
        if char.isalpha():
            if char.lower() in string and char.upper() in string:
                continue
            if string.count(char) == 1:
                repeated_letter += char
                break
        else:
            if string.count(char) == 1:
                repeated_letter += char
                break
    return repeated_letter

print(first_non_repeated_letter("~><#~><"))

