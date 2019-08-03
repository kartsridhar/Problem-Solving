#!/bin/python3

import math
import os
import random
import re
import sys

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arrSort = sorted(arr)
    indices = [None] * len(arr)
    for i in range(len(arr)):
        indices[i] = arrSort.index(arr[i])
    
    swapCount = 0
    for j in range(len(arr)):
        if j != indices[j]:
            swap(indices, j, indices.index(j))
            swapCount += 1
        pass
    return swapCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
