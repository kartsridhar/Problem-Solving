#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstrings' function below.
#
# The function accepts STRING s as parameter.
#

def findSubstrings(s):
    # Write your code here
    # start iterating from the 0th index of the string. if it is a vowel, start a new loop from i+1 and check if that character is a consonant. 
    # If it is a consonant, append it to the results 
    # sort the results in the end and the return [0] and [-1] elements of the result list.
    
    s.lower()
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    result = []
    for i in range(len(s)):
        if s[i] in list(vowels):
            for j in range(i+1, len(s)):
                if s[j] in list(consonants):
                    result.append(s[i:j+1])
    result.sort()
    print(result[0])
    print(result[-1])



if __name__ == '__main__':
    s = input()

    findSubstrings(s)
