#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    if len(arr) == 1:
        return "YES"

    leftSum = 0
    rightSum = sum(arr[1:])
    i = 1
    while i < len(arr):
        if leftSum == rightSum:
            return "YES"
        leftSum += arr[i-1]
        rightSum -= arr[i]
        i += 1
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
