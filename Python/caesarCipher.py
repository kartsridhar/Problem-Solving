#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    s = input()
    k = int(input())
    encrypted=""
    for i in s:
        if ord(i) in range(65, 91):
            new = chr(65+(ord(i)-65+k)%26)
            encrypted += new
        elif ord(i) in range(97, 123):
            new = chr(97+(ord(i)-97+k)%26)
            encrypted += new
        else:
            encrypted += i
    print(encrypted)