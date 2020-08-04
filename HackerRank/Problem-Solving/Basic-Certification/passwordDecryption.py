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

# Function to get all the numbers in the password
def getAllNumbers(s):
    nums = []
    for i in range(len(s)):
        if s[i].isnumeric() and s[i] != '0':
            nums.append(s[i])
    
    # Returning the reversed list as we want to swap the 0s in order
    return nums[::-1]

# Function to replace all the 0s with the respective original numbers
def replaceAllNumbers(s):
    nums = getAllNumbers(s)
    numIndex = 0            # index to access from the nums list
    s_new = ""              # updated encrypted password string to return
    for i in range(len(s)):
        if s[i] == '0':     # if it is 0, append the respective number from nums at numIndex to the new string
            s_new += nums[numIndex]
            numIndex += 1
        else:               # otherwise, just append the respective character
            s_new += s[i]
    
    # Since the encrypted password contains the numbers at the start, returning the replaced numbers by trimming all the numbers at
    # the start
    return s_new[len(nums):]

# Function to get all the substrings to replace the *s with
def getAllStars(s):
    s = replaceAllNumbers(s)
    s = s[::-1]             # reversing the string to make it easier
    substrings = []         # list to store the substrings to replace the *s with
    for i in range(len(s)-1):
        if s[i] == '*':
            substrings.append(s[i+1:i+3] + '$')     # since the string is reversed, store the respective slice delimited with a $ symbol
                                                    # this is to ensure that the substring to replace the encryptions are of the same length
    
    # Returning the substrings list reversed as we reversed the string initially
    return substrings[::-1]

def decryptPassword(s):
    # Write your code here
    substrings = getAllStars(s)
    starIndex = 0               # index to access from the substrings list
    s = replaceAllNumbers(s)    # replacing all the numbers of the string
    s_copy = s                  # working with a copy of the string to do all the replacements
    for i in range(len(s)):
        if s[i] == '*':
            # if a star is found, replace the previous 2 characters and the * with the respective substring
            s_copy = s_copy.replace(s_copy[i-2:i+1], substrings[starIndex])
            starIndex += 1
    
    # remove all the $ delimiters
    s_copy = s_copy.replace('$', '')
    return s_copy


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = '43Ah*ck0rr0nk'

    result = decryptPassword(s)
    # print(result)

    # fptr.write(result + '\n')

    # fptr.close()
