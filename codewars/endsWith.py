"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).
"""
#without using the endswith built in method

def solution(string, ending):
    # your code here...
    ending_len = len(ending)
    #if the ending is empty just return true
    if ending_len == 0:
        return True
    if string[-ending_len:] == ending:
        return True
    return False


print(solution("ninja", "ja"))