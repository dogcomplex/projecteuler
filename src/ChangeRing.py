import multiprocessing
from multiprocessing import *
import time

def nextP(P):
    i = 5
    while (i >=0 and P[i]>P[i+1]):
        i-=1
    if (i<0):
        return False
    k = 6
    while (P[i] > P[k]):
        k-=1
    t = P[i]
    P[i] = P[k]
    P[k] = t
    k=0
    for j in range(i+1, (7+i)/2+1):
        t = P[j]
        P[j] = P[7-k-1]
        P[7-k-1] = t
        k+=1
    return True

def rank(P):
    FACT = [720,120,24,6,2,1,0]
    list = [1,2,3,4,5,6,7]
    rank = 0
    for i in range(7):
        j=0
        while(P[i]!=list[j]):
            j+=1
        rank += j*FACT[i]
        for j in range(j,7-1):
            list[j]=list[j+1]
    return rank

def swap(P, skip):
    sw = -1
    for i in range(7):
        if (i != skip-1):
            if (sw<0):
                sw = i
            else:
                t = P[i]
                P[i] = P[sw]
                P[sw]=t
                sw = -1
 
class node:
    def __init__ (self, rank, history, depth, swaptype, parent=None):
        self.rank   = rank
        self.history    = history
        self.depth = depth
        self.swaptype = swaptype
        self.parent = parent
    def p(self):
        
        L=[]
        for i,x in enumerate(self.history):
            if (x >= 0):
                L.append(i)
        print self.rank, len(L), self.depth, self.swaptype, self.parent


def buildEdges():
    SWAPS = {}
    P = [1,2,3,4,5,6,7]
    notdone = True
    i=0
    while(notdone):
        D ={}
        j=0
        for L in [[3,1,3,1,3], [1,3,1,3,1],[5],[7]]:
            X=[]
            X.extend(P)
            B=[] 
            for skip in L:
                swap(X,skip)
                B.append(rank(X))
            C = []
            C.extend(B)
            D[j]=C
            j+=1
        SWAPS[i] = D    
        i+=1    
        #print i,P,D
        notdone=nextP(P)
    return SWAPS
        
def expand(n,SWAPS):
    H=[]
    H.extend(n.history)
    r = n.rank
    for child in SWAPS[n.rank][n.depth%2]:
        if (H[child]>=0):
            return []
        else:
            H[child]=r
            r = child
    if (H[SWAPS[r][2][0]]<0 and H[SWAPS[r][3][0]]<0):
        I = []
        I.extend(H)
        H[SWAPS[r][2][0]]=r
        I[SWAPS[r][3][0]]=r
        return [node(SWAPS[r][2][0],H,n.depth+1,5,n.rank) , node(SWAPS[r][3][0],I,n.depth+1,7,n.rank)]
    if (H[SWAPS[r][2][0]]<0):    
        H[SWAPS[r][2][0]]=r
        return [node(SWAPS[r][2][0],H,n.depth+1,5,n.rank)]
    if (H[SWAPS[r][3][0]]<0):
        H[SWAPS[r][3][0]]=r
        return [node(SWAPS[r][3][0],H,n.depth+1,7,n.rank)]
    return []

def backtrack(rank,history,depth,swaptype,parent,SWAPS):
    H =[]
    H.extend(history)
    if (depth>=839):
        print history
    #print swaptype
    r = rank
    for child in SWAPS[rank][depth%2]:
        if (H[child]>=0):
            return
        else:
            H[child]=r
            r = child
    if (H[SWAPS[r][2][0]]<0):
        H[SWAPS[r][2][0]]=r
        backtrack(SWAPS[r][2][0], H, depth+1, 5, rank, SWAPS)
        H[SWAPS[r][2][0]]=-1
    if (H[SWAPS[r][3][0]]<0):
        H[SWAPS[r][3][0]]=r
        backtrack(SWAPS[r][3][0], H, depth+1, 7, rank, SWAPS)
        H[SWAPS[r][3][0]]=-1
    return
    
def run2(L):
    n = L[0]
    SWAPS = L[1]
    backtrack(n.rank,n.history,n.depth,n.swaptype,n.parent,SWAPS)
    print "one node down..."

          
''' this has driven me crazy with unexplained deadlock. Forget this.      
def run(q,SWAPS):
    print "thread starting"
    
    primer = True
    while( not q.empty()):
            print q.qsize()
            n = q.get()
            n.p()
            #print n.depth
            if(n.depth>=839):
                #print n
                n.p()
                #return n
            
            if (primer):
                print "priming"
                for p in expand(n,SWAPS):
                    print "putting"
                    q.put(p)
                if (q.qsize() > 40):
                    primer = False
            else:
                print "backtracking"
                if (q.size() < 10):
                    primer = True
                    continue
                backtrack(n.rank, n.history, n.depth, n.swaptype, n.parent,SWAPS)
                print "done backtrack"
'''
        
def changering():    
    
    SWAPS = buildEdges()
    print "done edges"
    
    #node
    n = node(0,[-1]*5040,0,0,-1)
    #backtrack(n.rank,n.history,n.depth,n.swaptype,n.parent,SWAPS)
    
    WORK = [(n,SWAPS)]
    while (len(WORK) < 40):
        n = WORK.pop()[0]
        for m in expand(n,SWAPS):
            WORK.append((m,SWAPS))
    
    pool = Pool(processes=4)
    result = pool.map(run2,WORK)
    print result.get()
    
    '''
    q = Queue()
    q.put(n)
    
    P = []
    for i in range(4):
        p = multiprocessing.Process(target=run, args=(q,SWAPS,))
        p.start()
        P.append(p)
        #time.sleep(10)
        
      
    time.sleep(10)
    live = True
    while (live):
        live = False
        for p in P:
            if (p.is_alive()):
                live = True
    
    print "exit"
    for p in P:
        p.terminate()
    '''
    #pool.map(step, L) 
    #while(L):
    #    step(L,SWAPS)
    
    #print SWAPS[746]
    #print SWAPS[37]
    # stats section
    '''
    L = []
    for i in range(5040):
        L.append([])
        
    for i in SWAPS:
        r=i
        for config in [[0,2,1,2],[0,2,1,3],[0,3,1,2],[0,3,1,3]]:
            for skip in config:
                for s in SWAPS[r][skip]:
                    L[i].append(s)
                r=s
                
            
    for i in L:
        #i.sort()
        print i
    ''' 
    
    
#MAIN    
if __name__ == "__main__":
    freeze_support()
    changering()