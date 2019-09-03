#!/usr/bin/python3
import random

def getDirtyCells(board):
    cells = []
    for i, r in enumerate(board):
        if 'd' in r:
            for j, c in enumerate(r):
                if c == 'd':
                    cells.append((i, j))
    return cells
            

def next_move(posx, posy, board):
    cells = getDirtyCells(board)
    corners1 = [(0, 0), (0, 1), (1, 0),
                (len(board) - 1, len(board) - 1), (len(board) - 1, len(board) - 2), (len(board) - 2, len(board) - 1), 
                (0, len(board) - 2), (0, len(board) - 1), (1, len(board) - 1),
                (len(board) - 2, 0), (len(board) - 1, 0), (len(board) - 1, 1)]
    if (posx, posy) not in cells:
        for i in cells:
            if i in corners1:
                cells = [i]
                break
    corners2 = [[1, 1], [1, 3], [3, 3], [3, 1]]
    x, y = min(cells, key=lambda q : abs(posx - q[0]) + abs(posy - q[1])) if len(cells) != 0 else random.choice(corners2)
    
    if y < posy:
        print("LEFT")
    elif y > posy:
        print("RIGHT")
    elif x < posx:
        print("UP")
    elif x > posx:
        print("DOWN")
    else:
        print("CLEAN")

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)