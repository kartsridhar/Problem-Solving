#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    dist = []
    dirts= []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'd':
                dr = i
                dc = j
                dirts.append([dr, dc])
                d1 = abs(posr - dr)
                d2 = abs(posc - dc)
                dist.append(d1 + d2)
    nearest = min(dist)
    idx = dist.index(nearest)
    nr = dirts[idx][0]
    nc = dirts[idx][1]

    dr = posr - nr
    dc = posc - nc

    if board[posr][posc] == 'd':
        print("CLEAN")
    elif dr != 0:
        if dr > 0:
            print("UP")
        else:
            print("DOWN")
    elif dc != 0:
        if dc > 0:
            print("LEFT")
        else:
            print("RIGHT")
    
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)