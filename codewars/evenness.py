def iq_test(numbers):
    indexEven = 0
    indexOdd = 0
    numEven = 0
    numOdd = 0
    nums = numbers.split(" ")

    for i in range(len(nums)):
        if int(nums[i]) % 2 == 0:
            numEven += 1
            indexEven = i + 1
        else:
            numOdd += 1
            indexOdd = i + 1
    if numEven == 1:
        print(indexEven)
    else:
        print(indexOdd)

iq_test("2 4 7 8 10")
iq_test("1 2 1 1 1")