#Problem        : Base Arithmetic
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
base10 = 0

for line in data :
    ints = []
    for i in range(len(line)):
        if line[i].isalpha():
            ints.append(int(line[i], 16))
        else:
            ints.append(int(line[i]))
    base = max(ints) + 1
    val = int(line, base)
    base10 += val
print(base10)
