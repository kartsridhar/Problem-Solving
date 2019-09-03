#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    zone = s[-2]+s[-1]
    hour = s[:2]
    x = int(hour)
    time = ""
    if zone == 'PM':
        if x < 12:
            x += 12
            time = str(x) + s[2:8]
        else:
            time = s[:8]
    elif zone == 'AM':
        if x == 12:
            time = "00" + s[2:8]
        else:
            time = s[:8]
    return time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
