def isSorted(num):
    digits = list(str(num))
    unique = list(set(digits))
    if digits != unique:
        return False
    else:
        return digits == list(sorted(digits))

def findLargestNumber(num):
    if num < 10:
        return num

    while num > 9:
        if not isSorted(num):
            num -= 1
        else:
            return num
    return 0

if __name__ == "__main__":
    num = int(input())
    result = findLargestNumber(num)
    print(result)
