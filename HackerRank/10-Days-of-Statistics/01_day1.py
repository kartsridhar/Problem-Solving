# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(x):
    n = len(x)
    if n%2 == 0: 
        return (x[n//2] + x[(n-1)//2])//2
    else: 
        return x[n//2] 

n = int(input())
x = list(map(int, input().split()))
x.sort()
q1 = median(x[:(n//2)])
q2 = median(x)
q3 = median(x[((n+1)//2):])
print(q1)
print(q2)
print(q3)