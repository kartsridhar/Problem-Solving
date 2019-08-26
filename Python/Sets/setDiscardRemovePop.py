n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())
for _ in range(n_commands):
    command = list(map(str, input().split()))
    operation = command[0]
    if operation == 'pop':
        s.pop()
    elif operation == 'discard':
        s.discard(int(command[1]))
    elif operation == 'remove':
        s.remove(int(command[1]))
print(sum(s))