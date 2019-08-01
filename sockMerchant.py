#!/bin/python3

import math
import os
import random
import re
import sys

def findUnique(ar):
    unique = []
    for i in ar:
        if i not in unique:
            unique.append(i)
    return unique 

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counts = []
    unique = findUnique(ar)
    result = 0
    for i in unique:
        count = 0
        for j in ar:
            if i == j:
                count += 1
        counts.append(count)    
    for c in counts:
        result += c // 2
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
