#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count = 0
    if len(a) > len(b):
        big = a
        small = b
    else:
        big = b
        small = a
    for i in small:
        if i in big:
            count += 1
            big = list(big)
            big[big.index(i)] = None
    result = len(small) + len(big) - 2*count
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
