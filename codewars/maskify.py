# return masked string
def maskify(cc):
    # convert the argument passed to a string to ensure we are working with a string
    cc = str(cc)
    # declare a variable to assign the unmasked digits, for dynamics
    unmasked = 4;
    # check if the string's length is greater than the "unmasked" value, if not return it
    if len(cc) < unmasked:
        print(cc)
    # if its longer, get the last 4 characters and store them in a variable
    last_four_digits = cc[-4:]
    cc = cc.replace(last_four_digits, "")
    # convert the remaining string part to a list which is iterable
    str_list = list(cc)
    # loop through the list replacing each digit with a "#"
    for i in range(len(str_list)):
        str_list[i] = "#"
    masked_string = "".join([i for i in str_list])
    # concatenate the hashtags str with the last four digits
    print(masked_string + last_four_digits)


maskify("11111111155448521211566885 75")