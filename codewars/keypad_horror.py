def computer_to_phone(numbers):
    #your code here
    obj = {
        "7": "1",
        "8": "2",
        "9": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "1": "7",
        "2": "8",
        "3": "9",
        "0": "0"
    }
    new_str = ""
    for i in list(numbers):
        new_str += obj[i]
    return new_str


print(computer_to_phone("94561"))