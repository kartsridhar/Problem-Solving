#!/bin/python3

import math
import os
import random
import re
import sys

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                swap(a, j, j + 1)
                count += 1
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
