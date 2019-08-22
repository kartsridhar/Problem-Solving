#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine = sorted(list(magazine))
    note = sorted(list(note))
    i = 0
    j = 0
    match = 0
    while i < len(note) and j < len(magazine):
        if note[i] == magazine[j]:
            match += 1
            i += 1
        j += 1
    if match == len(note):
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
