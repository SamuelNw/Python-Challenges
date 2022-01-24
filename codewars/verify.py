#a function that verifies pin values to be all digits and exactly 4 or 6 digits

def verify(string):
    if string.isdigit():
        if len(string) == 4 or len(string)== 6:
            return True
        else:
            return False
    else:
        return False

print(verify("7552"))