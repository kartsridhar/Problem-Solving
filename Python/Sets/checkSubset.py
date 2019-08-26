# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    l1_len = int(input())
    l1 = list(map(int, input().split()))
    l2_len = int(input())
    l2 = list(map(int, input().split()))
    print(set(l1).issubset(set(l2)))