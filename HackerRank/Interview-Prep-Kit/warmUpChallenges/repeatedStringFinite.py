#!/bin/python3

import math
import os
import random
import re
import sys

def countA(s):
    count = 0
    for i in s:
        if i == 'a':
            count += 1
    return count

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    string1 = s * (n // len(s))
    remLength = n - len(string1)
    string2 = s[:remLength]
    finalString = string1 + string2
    count = countA(finalString)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
