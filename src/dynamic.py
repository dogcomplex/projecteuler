'''
Created on 2011-01-16
@author: Warren Koch, V00482478

Implementation of Smith-Waterman algorithm for local sequence alignment

Since Python is almost equal to pseudocode, and this would have been hell to program without it,
certainly on paper, I hope you don't mind this format!

The algorithm looks for a section of the sequences where the maximum score can be found, then
returns a local alignment sequence containing that max by constructing it from the table.
In other words: step one, compute the table, disallowing negative scores (since we are looking for maximum local score)
step two: find the max (I combine this with step 1)
step three: generate a sequence alignment using the table and max which uses the max local alignment
'''

''' Scoring constants '''
GAPSCORE = -2
LEFTSCORE = GAPSCORE
UPSCORE = GAPSCORE
MATCHSCORE = 1
MUTSCORE = -1


''' generates table dynamically according to constants, as well as returns the maximum value in the table '''
def localAlign(X,Y):
    n = len(X)
    m = len(Y)
    
    ''' init max '''
    maxval = 0
    maxij = (0,0)
    
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
            if i==0 or j==0:
                ''' set starting col/row to 0 '''
                C[i][j]= 0
            else:
                up = C[i-1][j] + UPSCORE
                left = C[i][j-1] + LEFTSCORE   
                if X[j-1]==Y[i-1]:
                    ''' match! (i-1,j-1 are for array-fitting purposes only)'''
                    diag = C[i-1][j-1] + MATCHSCORE
                else:
                    ''' mutation '''
                    diag = C[i-1][j-1] + MUTSCORE
                
                ''' the big equation! '''
                C[i][j]= max(0,left,up,diag)
            
            ''' update max for use in recovering sequence '''        
            if C[i][j] >= maxval:
                maxval = C[i][j]
                maxij = (i,j)      
    return C, maxij
        
        
''' reverses through the table to get sequence.  Assumes correctly generated table '''
def getseq(C,X,Y, maxij):
    S1 = []
    S2 = []
    i,j = maxij
    
    ''' go left and up from the max '''
    while i>0 or j>0:
        if j==0 or (i>0 and C[i-1][j] + UPSCORE == C[i][j]):
            ''' go up if the score fits, or at the leftmost column '''
            S1.insert(0,'-')
            S2.insert(0,Y[i-1])
            i-=1
        elif i==0 or (j>0 and C[i][j-1] + LEFTSCORE == C[i][j]):
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
              
    i,j = maxij
    ''' go down and right from the max '''
    while i<len(Y) or j<len(X):
        if j==len(X) or (i<len(Y) and C[i][j] + LEFTSCORE == C[i+1][j]):
            ''' go down if the score fits or at rightmost col'''
            S1.append('-')
            S2.append(Y[i])
            i+=1
        elif i==len(Y) or (j<len(X) and C[i][j] + UPSCORE == C[i][j+1]):
            ''' go right if the score fits or at bottom row'''
            S1.append(X[j])
            S2.append('-')
            j+=1
        else:
            ''' go diagonal '''
            S1.append(X[j])
            S2.append(Y[i])
            i+=1
            j+=1
    
    return S1,S2


'''
MAIN
'''

X = "localalignmentsaretrickier"
Y = "thanglobalxalignments"
C,maxij = localAlign(X,Y)

''' print table '''
for row in C:
    print row
print

print 'local alignment max =',  C[maxij[0]][maxij[1]], 'at', maxij
print

''' get aligned sequence '''
S = getseq(C,X,Y,maxij)
for V in S:
    s = ''
    for c in V:
        s += c
    print s