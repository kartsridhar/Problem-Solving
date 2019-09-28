def fibonacci(n):
    # Write your code here.
    return n if n<2 else fibonacci(n-1)+fibonacci(n-2)

n = int(input())
print(fibonacci(n))