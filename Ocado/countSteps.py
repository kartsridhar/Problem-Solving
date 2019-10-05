# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    num = int(S, 2)
    count = 0
    while num != 0:
        if num%2 == 0:
            num /= 2
        else:
            num -= 1
        count += 1
    return count
