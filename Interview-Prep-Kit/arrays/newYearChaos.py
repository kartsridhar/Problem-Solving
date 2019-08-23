#!/bin/python3

import math
import os
import random
import re
import sys

def swap(q, i, j):
    temp = q[i]
    q[i] = q[j]
    q[j] = temp

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    for _ in range(2):
        for i in range(len(q) - 1, 0, -1):
            if q[i] < q[i-1]:
                swap(q, i, i-1)
                count += 1
    if q != sorted(q):
        print("Too chaotic")
    else:
        print(count)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
