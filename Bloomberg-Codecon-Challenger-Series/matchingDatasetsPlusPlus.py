#Problem        : Matching Datasets++
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

k = int(input())
old, new = [], []

for i in range(k):
    data = list(map(float, input().split(',')))
    old.append(data)
for i in range(k):
    data = list(map(float, input().split(',')))
    new.append(data)

def compute_diff(a, b):
    total = 0.0
    for i in range(len(a)):
        total += abs(a[i] - b[i])
    return total

def min_index(mins):
    m, idx = mins[0], 0
    for i in range(len(mins)):
        if mins[i] < m:
            m, idx = mins[i], i
    return idx
    
for i in range(k):
    mins = []
    for j in range(k):
        mins.append(compute_diff(old[i], new[j]))
    print(str(i) + ',' + str(min_index(mins)))