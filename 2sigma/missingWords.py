#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the missingWords function below.
def missingWords(s, t):
    s = s.split(' ')
    t = t.split(' ')
    result = []
    j=0
    for i in range(len(s)):
        if j<len(t) and s[i]==t[j]:
            j += 1
        else:
            result.append(s[i])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    res = missingWords(s, t)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()
