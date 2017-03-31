

def missingNumbers(nums):
        # https://www.careercup.com/question?id=5753739085348864
    if not nums:
        return "0-99"
    output = ""
    count = 0
    for num in nums:
        if num > count:
            if num - 1 != count:
                rhs = "-" + str(num - 1) + ","
            else:
                rhs = ","
            output += str(count) + rhs
            count = num + 1
        else:
            count += 1

    if count < 99:
        if count == 0:
            count += 1

        output += str(count) + "-99"
    return output

print(missingNumbers([3, 5]))
print(missingNumbers([0]))
print(missingNumbers([3, 5]))
print(missingNumbers([0, 1, 2, 50, 52, 75]))
