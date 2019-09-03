#
def nextMove(n,r,c,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                pR = i
                pC = j
    move = ""
    dR = r - pR
    dC = c - pC
    
    if dR != 0:
        if dR > 0:
            move = "UP"
        else:
            move = "DOWN"
    elif dC != 0:
        if dC > 0:
            move = "LEFT"
        else:
            move = "RIGHT"

    return move

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))