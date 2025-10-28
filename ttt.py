
import math
def print_board(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==-1:
                print("  ",end="")
            elif a[i][j]==1:
                print(" O",end="")
            elif a[i][j]==0:
                print(" X",end="")
            if j!=len(a[i])-1:
                print(" | ",end="")
        print()
        if i!=len(a)-1:print("───┼────┼───")


def win(a):
    for i in range(3):
        if a[i][0]!=-1 and a[i][0]==a[i][1]==a[i][2]:
            return a[i][0]
        if a[0][i]!=-1 and a[0][i]==a[1][i]==a[2][i]:
            return a[0][i]
    if a[0][0]!=-1 and a[0][0]==a[1][1]==a[2][2]:
        return a[0][0]
    if a[0][2]!=-1 and a[0][2]==a[1][1]==a[2][0]:
        return a[0][2]
    return -1

def full_board(a):
    for r in range(3):
        for c in range(3):
            if a[r][c]==-1:
                return False
    return True

def minimax(a,depth,flag,turn):
    score=win(a)
    if score!=-1:
        if score==turn:
            return 10-depth
        else:
            return depth-10
    if full_board(a):
        return 0
    best=-1000 if flag else 1000
    for i in range(3):
        for j in range(3):
            if a[i][j]==-1:
                a[i][j]=turn if flag else 1-turn
                value=minimax(a,depth+1,not flag,turn)
                best=max(best,value) if flag else min(best,value)
                a[i][j]=-1
    return best

def evaluate(a,turn):
    best_x=0
    best_y=0
    best_num=-math.inf
    for row in range(3):
        for col in range(3):
            if a[row][col]==-1:
                a[row][col]=turn
                cnt_num=minimax(a,0,False,turn)
                a[row][col]=-1
                if cnt_num>best_num:
                    best_num=cnt_num
                    best_x=row
                    best_y=col
    return best_x,best_y


board=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
x,y=evaluate(board,1)
board[x][y]=1
print_board(board)