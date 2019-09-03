# Enter your code here. Read input from STDIN. Print output to STDOUT
dimensions = list(map(int, input().split()))
N = dimensions[0]
M = dimensions[1]
for i in range(1, N - 1, 2):
    string = '.|.'
    print((string * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N - 2, 0, -2):
    string = '.|.'
    print((string * i).center(M, '-'))
