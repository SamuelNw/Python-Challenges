"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.
"""
import string
def alphabet_position(text):
    alpha_dict = {string.ascii_lowercase[i] : [num for num in range(1, 27)][i] for i in range(len(string.ascii_lowercase))}
    text = text.lower().strip()

    answer = []
    for char in list(text):
        if char in alpha_dict.keys():
            for key, value in alpha_dict.items():
                if key == char:
                    answer.append(str(value))
        else:
            continue

    print(" ".join(answer))

alphabet_position("The sunset sets at twelve o' clock.")