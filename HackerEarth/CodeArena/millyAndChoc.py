'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

INPUT
1
3 2
1 KITKAT
2 FIVESTAR KITKAT
2 KITKAT PERK

OUTPUT
1
'''

# Write your code here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    count = -1
    for i in range(n):
        room = list(input().split())
        num = int(room[0])
        chocs = room[1:]
        if len(set(chocs)) >= k:
            count = i
            break
    print(count)
    