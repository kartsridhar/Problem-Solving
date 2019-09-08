'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n, q = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(q):
    op = list(map(int, input().split()))
    command = op[0]
    if command == 1:
        x = op[1]-1
        arr[x] = 0 if arr[x] == 1 else 1
    elif command == 0:
        r = op[2]-1
        print("EVEN" if n[r] == 0 else "ODD")

