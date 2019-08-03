#!/bin/python3


# This is the first version of the challenge. Complicated and Naive, doesn't pass all tests. 
# The other file contains a valid, simpler and faster solution 

import math
import os
import random
import re
import sys

def powerset(prices):
    pset = [[]]
    for p in prices:
        pset += [i + [p] for i in pset]
    pset.remove([])
    return pset

# Complete the maximumToys function below.
def maximumToys(prices, k):
    list1 = []
    for i in range(len(prices)):
        if prices[i] < k:
            list1.append(prices[i])
    list2 = []
    pset = powerset(list1)
    for j in range(len(pset)):
        if sum(pset[j]) < k:
            list2.append(pset[j])
    list3 = []
    for k in range(len(list2)):
        list3.append(len(list2[k]))
    best = max(list3)
    return best

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
