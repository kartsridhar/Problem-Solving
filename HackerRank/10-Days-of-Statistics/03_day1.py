# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median 
n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))
data = []
for i in range(n):
    for j in range(f[i]):
        data.append(x[i])
data.sort()
q1 = median(data[:sum(f)//2])
q3 = median(data[(sum(f)+1)//2:])
print('%0.1f' % (q3-q1))