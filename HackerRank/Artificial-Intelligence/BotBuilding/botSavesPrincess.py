#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                mX = i
                mY = j
            if grid[i][j] == 'p':
                pX = i
                pY = j
    
    for _ in range(int(n/2)):
        if pX < mX:
            print("UP")
            if pY == 0:
                print("LEFT")
            else:
                print("RIGHT")
        else:
            print("DOWN")
            if pY == n - 1:
                print("RIGHT")
            else:
                print("LEFT")
    
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)