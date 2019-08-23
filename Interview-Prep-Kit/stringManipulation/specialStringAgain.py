#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    for k, v in enumerate(s):
        i = None
        for j in range(k+1, n):
            if v == s[j]:
                if i is None:
                    count += 1
                elif j - i == i - k:
                    count += 1
                    break
            else:
                if i is None:
                    i = j
                else:
                    break
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
