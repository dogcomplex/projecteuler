'''
Created on 2011-01-16
@author: Warren Koch, V00482478
'''

''' Scoring constants '''
GAPSCORE = -2
LEFTSCORE = GAPSCORE
UPSCORE = GAPSCORE
MATCHSCORE = 1
MUTSCORE = -1


''' generates table dynamically '''
def localAlign(X,Y):
    n = len(X)
    m = len(Y)
    
    '''
    initiate array. (just for ease of display, could do on the fly
    instead but it would look more complicated with Python)
    first row and col are for empty sequences of Y and X respectively
    '''
    C = []
    for i in range(m+1):
        C.append([])
        for j in range(n+1):
            C[i].append(0)

    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                if j==0:
                    ''' top left corner '''
                    C[i][j]=0
                else:
                    ''' top row, only choice is left '''
                    left = C[i][j-1] + LEFTSCORE
                    C[i][j]= left
            else:
                up = C[i-1][j] + UPSCORE
                if j==0:
                    ''' left col, only choice is up '''
                    C[i][j]=up
                else:
                    left = C[i][j-1] + LEFTSCORE   
                    if X[j-1]==Y[i-1]:
                        ''' match! '''
                        diag = C[i-1][j-1] + MATCHSCORE
                    else:
                        ''' mutation '''
                        diag = C[i-1][j-1] + MUTSCORE
                    
                    ''' the big equation! '''
                    C[i][j]= max(left,up,diag)      
    return C
        
        
''' reverses through the table to get sequence.  Assumes correctly generated table '''
def getseq(C,X,Y):
    S1 = []
    S2 = []
    i = len(Y)
    j = len(X)
    
    while i>0 or j>0:
        if j==0 or C[i-1][j] + UPSCORE == C[i][j]:
            ''' go up if the score fits, or at the leftmost column '''
            S1.insert(0,'-')
            S2.insert(0,Y[i-1])
            i-=1
        elif i==0 or C[i][j-1] + LEFTSCORE == C[i][j]:
            ''' go left if the score fits, or at the top row '''
            S1.insert(0,X[j-1])
            S2.insert(0,'-')
            j-=1
        else:
            ''' go diagonal '''
            S1.insert(0,X[j-1])
            S2.insert(0,Y[i-1])
            i-=1
            j-=1
    return S1,S2



X = "example"
Y = "sample"
C = localAlign(X,Y)

''' print table '''
for row in C:
    print row

''' get aligned sequence '''
S = getseq(C,X,Y)
for V in S:
    print V