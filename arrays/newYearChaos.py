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
    bribeCount = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(i + 1, len(q)):
            if q[i] > q[j]:
                swap(q, j, i)
                bribeCount += 1
    print(bribeCount)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
