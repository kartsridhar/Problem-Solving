'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(q):
    num, l, r = list(map(int, input().split()))
    l -= 1
    isA, isB = False, False
    if num == 1:
        isA = True
    else:
        isB = True
    
    total = 0
    for i in range(l,r):
        if isA:
            total += a[i]
            isA = not isA
            isB = not isB
            continue
        if isB:
            total += b[i]
            isA = not isA
            isB = not isB
            continue
    print(total)
