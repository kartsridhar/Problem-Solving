# Enter your code here. Read input from STDIN. Print output to STDOUT
length = int(input())
original_set = set(map(int, input().split(' ')))
N = int(input())

for i in range(N):
    command = input().split(' ')
    new_set = set(map(int, input().split(' ')))
    if command[0] == 'intersection_update':
        original_set.intersection_update(new_set)
    elif command[0] == 'update':
        original_set.update(new_set)
    elif command[0] == 'symmetric_difference_update':
        original_set.symmetric_difference_update(new_set)
    elif command[0] == 'difference_update':
        original_set.difference_update(new_set)
print(sum(original_set))
