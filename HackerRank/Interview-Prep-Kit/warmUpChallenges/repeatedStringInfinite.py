#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count1 = 0
    count2 = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count1 += 1
            if i < (n % len(s)):
                count2 += 1
    total = count1 * (n // len(s)) + count2
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
