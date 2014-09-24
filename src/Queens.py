'''
Created on 2009-10-07

@author: Warren
'''
n = 5
Q = [0]*n
a = [True]*n
b = [True]*(2*n)
c = [True]*(2*n)

def Queens(col):
    global n, Q, a,b,c
    for row in range(n):
        if a[row] and b[row+col] and c[n+row-col]:
            Q[col] = row
            if col == n-1:
                print(Q)
            else:    
                a[row] = b[row+col]=c[n+row-col]=False
                Queens(col+1)
                a[row] = b[row+col]=c[n+row-col]=True
        
n = 5
Q = [0]*n
a = [True]*n
b = [True]*(2*n-2)
c = [True]*(2*n)
d = [True]*(2*n)

          
def makeQueen(col, row, n):
    Q = 0
    Q |= (2**n) << (n*col)
    for i in range(col):
        
    
def Queens2(col,row):
    global n, Q, a,b,c
    print(col,row, a,b,c)
    queen = makeQueen(col,row,n)
    if a[row] or b[row+col-2] or c[n+row-col] or d[col]:
        Q[col] = row
        if True not in a and True not in b and True not in c and True not in d:
            print(Q)
            return
        a[row] = b[row+col-2]=c[n+row-col]=False
        if row < n-1:
            Queens2(col,row+1)
        else:
            Queens2(col+1,0)
        a[row] = b[row+col]=c[n+row-col]=True
        
Queens2(0,0)

m=5
n=5
k=1
pos=1
TheBoard = 0
PieceAvail = range(1,13)
Solution = [0]*13
List = [[]]*n

def BuildPieces(m,n):
    global List, PieceAvail
    Pieces = [[]]*12
    for pc in Pieces:
        pc.append(1)
        #whatever.
    
def Pentomino(k, pos):
    global TheBoard, PieceAvail, List, Solution
    while pos & TheBoard != 0:
        pos <<=1
        k +=1
    for pc in range(1,13):
        if pc in PieceAvail:
            PieceAvail -= pc
            PieceConfigs = List[pc][k]
            for i,p in enumerate(PieceConfigs):
                Solution[pc] = i 
                if TheBoard & p == 0:
                    TheBoard |= p
                    if PieceAvail == []:
                        print(Solution)
                    else:
                        Pentomino(k+1,pos<<1)
                    TheBoard ^= p
            PieceAvail += pc 
            
