#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def getAllNumbers(s):
    nums = []
    for i in range(len(s)):
        if s[i].isnumeric() and s[i] != '0':
            nums.append(s[i])
    return nums[::-1]

def replaceAllNumbers(s):
    nums = getAllNumbers(s)
    numIndex = 0
    s_new = ""
    for i in range(len(s)):
        if s[i] == '0':
            s_new += nums[numIndex]
            numIndex += 1
        else:
            s_new += s[i]
    return s_new[len(nums):]

def getAllStars(s):
    s = replaceAllNumbers(s)
    s = s[::-1]
    substrings = []
    for i in range(len(s)-1):
        if s[i] == '*':
            substrings.append(s[i+1:i+3] + '$')
    return substrings[::-1]

def decryptPassword(s):
    # Write your code here
    substrings = getAllStars(s)
    starCount = 0
    s = replaceAllNumbers(s)
    s_copy = s
    for i in range(len(s)):
        if s[i] == '*':
            s_copy = s_copy.replace(s_copy[i-2:i+1], substrings[starCount])
            starCount += 1
    s_copy = s_copy.replace('$', '')
    return s_copy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = decryptPassword(s)

    fptr.write(result + '\n')

    fptr.close()
