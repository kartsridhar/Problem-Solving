#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    zone = s[-2]+s[-1]
    if zone == 'PM':
        hour = s[:2]
        x = int(hour)
        if x < 12:
            x += 12
    time = str(x) + s[2:8]
    return time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
