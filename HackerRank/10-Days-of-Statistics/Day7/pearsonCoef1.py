# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

import statistics as s
muX = s.mean(x)
muY = s.mean(y)
stdX = s.pstdev(x)
stdY = s.pstdev(y)
print(round(sum((x[i]-muX)*(y[i]-muY) for i in range(n))/(n*stdX*stdY), 3))