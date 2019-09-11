# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean, std = map(float, input().split())
q1 = float(input())
q23 = float(input())
phi = lambda m, v, val : 0.5 * (1+math.erf((val-m)/(v*math.sqrt(2))))
print(round(100 - (phi(mean, std, q1)*100), 2))
print(round(100 - (phi(mean, std, q23)*100), 2))
print(round(phi(mean, std, q23)*100, 2))