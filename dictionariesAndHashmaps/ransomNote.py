#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine = list(magazine)
    note = list(note)
    match = []
    for i in note:
        if i in magazine:
            match.append(True)
            magazine.remove(i)
        else:
            match.append(False)
    if all(match):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
