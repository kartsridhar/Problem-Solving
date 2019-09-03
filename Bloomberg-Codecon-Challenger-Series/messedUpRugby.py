#Problem        : Messed up Rugby
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

score = int(data[0])
possibilities = []
for x in range((score//7)+1):
    for y in range((score//3)+1):
        for z in range((score//2)+1):
            if 7*x + 3*y + 2*z == score:
                possibilities.append([x, y, z])

for i in range(len(sorted(possibilities))):
    print(str(possibilities[i][0]) + " " + str(possibilities[i][1]) + " " + str(possibilities[i][2]))