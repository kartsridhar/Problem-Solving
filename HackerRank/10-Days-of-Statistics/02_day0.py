# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(float, input().split()))
w = list(map(float, input().split()))
weighted = sum(i*j for i, j in zip(x, w))
avg = weighted/sum(w)
print('%.1f' % avg)