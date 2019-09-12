# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = float(input())
mean = float(input())
std = float(input())
p = float(input())
z = float(input())
cl = z*(std/math.sqrt(n))
print(round(mean-cl, 2))
print(round(mean+cl, 2))