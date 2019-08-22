#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def nCr(s, n, r):
    return s[n] * (s[n] - 1) // r

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    substringCount = Counter()
    anagramCount = 0

    for i in range(len(s)):
        substrings = []
        for j in range(len(s) - i):
            substrings.append("".join(sorted(s[j:j+i+1])))
        substringCount.update(substrings)
    
    for k in substringCount:
        anagramCount += nCr(substringCount, k, 2)
    
    return anagramCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
