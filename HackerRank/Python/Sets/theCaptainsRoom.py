# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
rooms = list(map(int, input().split()))
unique_rooms, duplicate_rooms = set(), set()
for i in rooms:
    if i in unique_rooms:
        duplicate_rooms.add(i)
    else:
        unique_rooms.add(i)
captain = list(unique_rooms.difference(duplicate_rooms))[0]
print(captain)