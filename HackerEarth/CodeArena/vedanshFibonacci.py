# Write your code here
def fibs(n):
    fibs = [1, 1]
    while fibs[-1] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    return "YES" if n in fibs else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    print(fibs(n))