"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains
an odd number of characters then it should replace the missing second character of the final
pair with an underscore ('_').
"""
def solution(s):
    x = "".join([word for word in list(str(s)) if word != " "])

    if len(x) == 1:
        return [i+"_" for i in list(x)]

    answer = []
    final_answer = []
    while len(str(x)) > 0:
        answer.append(str(x)[:2])
        x = str(x)[2:]
    for pair in answer:
        if len(pair) < 2:
            pair = pair + "_"
        final_answer.append(pair)

    return final_answer




print(solution("ub"))