#Problem        : Laundry Day
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
laundry = []

for line in data :
    laundry.append(line)
output = []
for i in set(laundry):
    count = laundry.count(i)
    if "sock" in i:
        if count % 2 != 0:
            pairs = count // 2
            output.append(str(pairs) + '|' + i)
            output.append('0' + '|' + i)
        else:
            pair = count // 2
            output.append(str(pair) + '|' + i)
    else:
        output.append(str(count) + '|' + i)
        
for j in sorted(set(output)):
    print(j)