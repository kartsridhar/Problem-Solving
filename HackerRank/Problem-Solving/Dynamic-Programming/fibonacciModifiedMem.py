#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fib(t1, t2, n, dp):
    if dp[n] != None:
        return dp[n]

    result = 0
    if n == 1:
        result = t1
    elif n == 2:
        result = t2
    else:
        result = fib(t1,t2,n-2,dp) + (fib(t1,t2,n-1,dp) ** 2)
    dp[n] = result
    return result

def fibonacciModified(t1, t2, n):
    dp = [None] * (n+1)
    return fib(t1,t2,n,dp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
