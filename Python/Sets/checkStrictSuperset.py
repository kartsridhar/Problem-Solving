# Enter your code here. Read input from STDIN. Print output to STDOUT
parent = list(map(int, input().split()))
n = int(input())
result = []
for _ in range(n):
    child = list(map(int, input().split()))
    check = set(parent).issuperset(set(child))
    result.append(check)
if all(result):
    print("True")
else:
    print("False")