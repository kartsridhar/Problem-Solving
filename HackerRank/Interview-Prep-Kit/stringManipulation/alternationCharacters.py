#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    s = list(s)
    s_copy = s
    for i, j in enumerate(s_copy[:-1]):
        if j == s_copy[i+1]:
            s_copy[i+1] = None
    return s_copy.count(None)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
