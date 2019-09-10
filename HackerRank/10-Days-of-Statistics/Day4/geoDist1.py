# Enter your code here. Read input from STDIN. Print output to STDOUT
num, den = map(int, input().split())
p = num/den
n = int(input())
g = lambda n, p : (1-p)**(n-1) * p
print(round(g(n, p), 3))