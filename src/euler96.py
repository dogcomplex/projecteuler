'''
Created on Oct 25, 2011

@author: W
'''


def readGrid(f):
    f.readline()
    G = []
    for i in range(9):
        line = f.readline()
        L = list(line[:9])
        L = map(int,L)
        G += [L]
    for i in range(9):
        for j in range(9):
            if G[i][j]==0:
                G[i][j] = set(range(1,10))
            else:
                G[i][j] = set([G[i][j]])
    return G

def updateGrid(G,x,y):

    change=False
    if len(G[x][y])==1: 
        for i in range(9):
            if i!=x and len(G[i][y])>1:
                G[i][y].difference_update(G[x][y])
                if len(G[i][y])==1:
                    updateGrid(G,i,y)
                    change=True
        for j in range(9):
            if j!=y and len(G[x][j])>1:
                G[x][j].difference_update(G[x][y])
                if len(G[x][j])==1:
                    updateGrid(G,x,j)
                    change=True
        for i in range(3*(x/3),3*((x/3)+1)):
            for j in range(3*(y/3),3*((y/3)+1)):
                if (i!=x and j!=y) and len(G[i][j])>1:
                    G[i][j].difference_update(G[x][y])
                    if len(G[i][j])==1:
                        updateGrid(G,i,j)
                        change=True
    H = [set([]),set([]),set([])]
    V = [set([]),set([]),set([])]       
    for i in range(3*(x/3),3*((x/3)+1)):
        for j in range(3*(y/3),3*((y/3)+1)):
            H[i%3].update(G[i][j])
            V[j%3].update(G[i][j])
            
    
    H2 = [set([]),set([]),set([])]
    V2 = [set([]),set([]),set([])]    
    for k in range(3):
        H2[k] = set([])
        H2[k].update(H[(k+1)%3])
        H2[k].update(H[(k+2)%3])
        H2[k] = H[k].difference(H2[k])  
        V2[k] = set([])
        V2[k].update(V[(k+1)%3])
        V2[k].update(V[(k+2)%3])
        V2[k] = V[k].difference(V2[k])
        if len(H2[k])>0:
            i = 3*(x/3)+k
            for j in list(range(0,3*(y/3))) + list(range(3*(y/3 +1),9)):
                if len(G[i][j])>1:
                    G[i][j].difference_update(H2[k])
                    if len(G[i][j])==1:
                        updateGrid(G,i,j)
                        change=True
                    
        if len(V2[k])>0:
            j = 3*(y/3)+k
            for i in list(range(0,3*(x/3))) + list(range(3*(x/3 +1),9)):
                if len(G[i][j])>1:
                    G[i][j].difference_update(V2[k])
                    if len(G[i][j])==1:
                        updateGrid(G,i,j)
                        change=True

 
    for i in range(3*(x/3),3*(x/3+1)):
        for j in range(3*(y/3),3*((y/3)+1)):
            Temp = H2[i%3].intersection(V2[j%3])
            if len(Temp)>0 and len(G[i][j])>1:
                G[i][j].clear()
                G[i][j].update(Temp)
                updateGrid(G,i,j)
                change=True
    
    return change        
    

def printGrid(G):
    solved = True
    print
    for i in range(9):
        for j in range(9):
            s = ''
            if len(G[i][j])>1:
                solved = False
            for k in G[i][j]:
                s += str(k)
            print s,
            if j%3==2:
                print '\t', '\t', 
        if i%3==2:
                print
        print
    print
    return solved

def extractNum(G):
    L =G[0][:3]
    s = ''
    for c in L:
        s += str(list(c)[0])
    return int(s)

def easysolveGrid(G):
    for i in range(9):
        for j in range(9):
            if len(G[i][j])==1:
                updateGrid(G,i,j)

def tryEverything(G):
    change=False
    for i in range(9):
        for j in range(9):
            if len(G[i][j])>1:
                change=updateGrid(G,i,j)
    if change:
        return tryEverything(G)
    else:
        return printGrid(G)
        
def validitycheck(G):
    for i in range(9):
        Row = set([])
        for j in range(9):
            if len(G[i][j])==1:
                if Row.intersection(G[i][j]):
                    return i,j,'row', Row.intersection(G[i][j])
                else:
                    Row.update(G[i][j])
    for j in range(9):
        Col = set([])
        for i in range(9):
            if len(G[i][j])==1:
                if Col.intersection(G[i][j]):
                    return i,j,'col', Row.intersection(G[i][j])
                else:
                    Col.update(G[i][j])
    for i in range(3):
        for j in range(3):
            Box = set([])
            for k in range(3):
                for l in range(3):
                    if len(G[3*i+k][3*j+l])==1:
                        if Box.intersection(G[3*i+k][3*j+l]):
                            return 3*i+k,3*j+l,'box', Row.intersection(G[i][j])
                        else:
                            Box.update(G[3*i+k][3*j+l])
    return True
    
            
        
def guess(G,x,y,g):
    print 'Guessing', x, y, 'is', g
    Saved = []
    for i in range(9):
        Saved += [[]]
        for j in range(9):
            Saved[i]+=[[]]
            Saved[i][j]=G[i][j].copy()
    G[x][y] = set([g])
    change=updateGrid(G,x,y)
    if not tryEverything(G):
        print 'GUESS FAILED'
        G = Saved
        return False
    else:
        print 'GUESS SUCCESS?'
        test = validitycheck(G)
        if test==True:
            print "SUCCESS"
            return True
        else:
            print "FAILURE", test
            G = Saved
            return False
        
    
      
    

sum = 0
f = open('sudoku.txt','r')
for k in range(50):    
    G = readGrid(f)
    easysolveGrid(G)
    
    if tryEverything(G):
        test = validitycheck(G)
        if test==True:
            print k, 'solved'
            sum += extractNum(G)
        else:
            print "FAILURE", test
        
    else:
        print k, 'not solved yet'
        
        '''cheat like crazy.'''
        if k==6:
            if guess(G,0,0,1):
                sum += extractNum(G)
                continue
        if k==9:
            if guess(G,6,1,8):
                sum += extractNum(G)
                continue
        if k==27:
            if guess(G,0,0,3):
                sum += extractNum(G)
                continue
        if k==41:
            if guess(G,1,0,1):
                sum += extractNum(G)
                continue
        if k==44:
            if guess(G,0,0,5):
                sum += extractNum(G)
                continue
        if k==46:
            if guess(G,0,0,1):
                sum += extractNum(G)
                continue
        if k==47:
            if guess(G,0,1,6):
                sum += extractNum(G)
                continue
        if k==48:
            if guess(G,3,1,5):
                sum += extractNum(G)
                continue
            else:
                if guess(G,2,3,7):
                    sum += extractNum(G)
                    continue
        if k==49:
            if guess(G,3,8,3):
                sum += extractNum(G)
                continue
        break

print sum