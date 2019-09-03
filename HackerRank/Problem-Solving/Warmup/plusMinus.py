#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos_ratio = sum(1 for x in arr if x > 0) / len(arr)
    neg_ratio = sum(1 for y in arr if y < 0) / len(arr)
    zero_ratio = sum(1 for z in arr if z == 0) / len(arr)
    print('%.6f' % pos_ratio)
    print('%.6f' % neg_ratio)
    print('%.6f' % zero_ratio)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
