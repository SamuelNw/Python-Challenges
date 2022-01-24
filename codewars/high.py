"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.
"""

import string

def high(x):
    #get a list for each of letters and their corresponding positions
    alpha_list = list(string.ascii_lowercase)
    num_list = [num for num in range(1, 27)]
    #create a dictionary with key being the letter and value its count
    char_dict = {alpha_list[i] : num_list[i] for i in range(len(alpha_list))}
    #get a list of strings from the given string x
    strings_list = x.lower().split(" ")
    #create an empty array to append the sum of counts of each word
    count_arr = []
    #loop through each word counting the sum of its letters count and append the sum to the array
    for word in strings_list:
        string_count = sum([char_dict[i] for i in list(word)])
        count_arr.append(string_count)
    #get a sorted array version for the count list to acquire the largest number from
    sorted_count_arr = sorted(count_arr)
    #create a new dict for the string and their sums for the letter count
    new_dict = {strings_list[i] : count_arr[i] for i in range(len(strings_list))}
    #loop through the dict and return the key with the largest value
    for key, value in new_dict.items():
        if value == sorted_count_arr[-1]:
            return key


print(high("I wanna become a code machine in the near future"))