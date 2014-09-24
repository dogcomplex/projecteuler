import multiprocessing
from multiprocessing import *
import time
import itertools
from math import *
import random


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
    L = [1,2,3,4,5,6,7]
    rank = 0
    for i in range(7):
        j=0
        while(P[i]!=L[j]):
            j+=1
        rank += j*FACT[i]
        for j in range(j,6):
            L[j]=L[j+1]
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
                r = rank(X)
                #print r, X
                B.append(r)
            C = []
            C.extend(B)
            D[j]=C
            j+=1
            print 
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

        

def backtrack(rank,depth,Classes,ClassMap,rankmap,SEQ,maxdepth):
    if depth>=maxdepth[0]:
        maxdepth[0] = depth
        print depth,SEQ
    c = ClassMap[rank]
    if Classes[c]<0:
        if depth >=838:
            print Classes
        Classes[c]=rank
        backtrack(rankmap[rank][0+depth%2],depth+1,Classes,ClassMap,rankmap,SEQ+[0],maxdepth)
        backtrack(rankmap[rank][2+depth%2],depth+1,Classes,ClassMap,rankmap,SEQ+[1],maxdepth)
        Classes[c]=-1
        
def track(rank,depth,Classes,ClassMap,rankmap,SEQ):
    #print depth
    c = ClassMap[rank]
    if Classes[c]<0:
        if depth >=838:
            print Classes
            return depth
        Classes[c]=rank
        d = track(rankmap[rank][2*SEQ[depth%len(SEQ)]+depth%2],depth+1,Classes,ClassMap,rankmap,SEQ)
        #Classes[c]=-1
        return d
    return depth
        
def run2((n,SWAPS)):
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
                 
        
def main():    
    
    SWAPS = buildEdges()
    print "done edges"
    
    #node
    n = node(0,[-1]*5040,0,0,-1)
    #backtrack(n.rank,n.history,n.depth,n.swaptype,n.parent,SWAPS)
    
    
    file = open('out.txt','w')
    

    ClassMap = [-1]*5040
    Classes = []
    count =0
    for i in range(5040):
        SWAPS[i][0].append(i)
        if ClassMap[i]<0:
            for r in SWAPS[i][0]:
                ClassMap[r]=count
            count +=1
            Classes.append(-1)
    
    #print ClassMap
    
    rankmap = []
    for i in range(5040):
        r3 =SWAPS[i][0][4]
        r1 =SWAPS[i][1][4]
        r35 =SWAPS[r3][2][0]
        r15 =SWAPS[r1][2][0]
        r37 = SWAPS[r3][3][0]
        r17 = SWAPS[r1][3][0]
        rankmap.append((r35,r15,r37,r17))
    
    #backtrack(0,0,Classes,ClassMap,rankmap)
        
    '''
    SEQS = []    
    Depths = []
    N=1
    maxdepth = 0
    while(N<50):
        for seq in itertools.product([0,1], repeat=N):
            maxperm = -1
            maxpermdepth = 0
            
            depth = backtrack(0,[-1]*5040,0,SWAPS,0,seq)
            if(depth>maxdepth):
                maxdepth = depth
                print maxdepth, seq
            SEQS.append(seq)
            Depths.append(maxdepth)
        N+=1
    '''
    
    '''
    WORK = [(n,SWAPS)]
    while (len(WORK) < 40):
        n = WORK.pop()[0]
        for m in expand(n,SWAPS):
            WORK.append((m,SWAPS))
    
    pool = Pool(processes=2)
    result = pool.map(run2,WORK)
    print result.get()
    '''
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
    '''
    SWAPS2 = []
    for P in itertools.permutations([1,2,3,4,5,6,7]):
        i=0
        T = []
        for H in [[3,1,3,1,3],[1,3,1,3,1]]:
            P = list(P)
            r=rank(P)
            SW = []
            for skip in H:
                print P
                swap(P,skip)
                print skip, P
                r = rank(P)
                #print r, skip,P 
                SW.append(r)
            T.append(SW)
            i+=1
        SWAPS2.append(T)
   '''
    class MyError(Exception):
        def __init__(self, max, PATH):
            self.max = max
            self.PATH = PATH
        def __str__(self):
            return repr(self.value)
   
    def backtrackSEQ(rank,depth,Classes,ClassMap,rankmap,SEQ,seqpos,maxdepth,PATH,fails,maxpath):
        if depth>=maxdepth[0]:
            maxdepth[0] = depth
            maxpath = []
            maxpath.extend(PATH)
            print depth,seqpos, fails,PATH
        c = ClassMap[rank]
        if Classes[c]<0:
            if depth >=838:
                print Classes
            #if fails[0] >10000000:
            #    raise MyError(maxdepth[0],PATH)
            Classes[c]=rank
            #choice = SEQ[seqpos%len(SEQ)]
            if seqpos<7:
                choice = 0
                seqpos +=1
            else:
                choice = 1
                seqpos = 0
            backtrackSEQ(rankmap[rank][choice*2+depth%2],depth+1,Classes,ClassMap,rankmap,SEQ,seqpos,maxdepth,PATH+[choice],fails,maxpath)
            choice = (choice+1)%2
            #fails[0]+=2000-2*depth
            backtrackSEQ(rankmap[rank][choice*2+depth%2],depth+1,Classes,ClassMap,rankmap,SEQ,seqpos,maxdepth,PATH+[choice],fails,maxpath)
            Classes[c]=-1
    
    def backtrackRepeat(rank,depth,Classes,ClassMap,rankmap,seqtype,LIMITS, seqpos,maxdepth,PATH,fails,maxpath):
        if depth>=maxdepth[0]:
            maxdepth[0] = depth
            maxpath = []
            maxpath.extend(PATH)
            print depth,seqtype, fails,PATH
        c = ClassMap[rank]
        if Classes[c]<0:
            if depth >=838:
                print Classes
            #if fails[0] >10000000:
            #    raise MyError(maxdepth[0],PATH)
            Classes[c]=rank
            #choice = SEQ[seqpos%len(SEQ)]
            if seqpos==LIMITS[seqtype]-1:
                seqpos = 0
                seqtype= (seqtype +1)%2
            else:
                seqpos+=1
            backtrackRepeat(rankmap[rank][seqtype*2+depth%2],depth+1,Classes,ClassMap,rankmap,seqtype,LIMITS,seqpos, maxdepth,PATH+[seqtype],fails,maxpath)
            seqtype = (seqtype+1)%2
            seqpos=0
            #fails[0]+=2000-2*depth
            backtrackRepeat(rankmap[rank][seqtype*2+depth%2],depth+1,Classes,ClassMap,rankmap,seqtype,LIMITS,seqpos, maxdepth,PATH+[seqtype],fails,maxpath)
            Classes[c]=-1

    def monoTrack(rank,depth,Classes,ClassMap,rankmap,swaptype,pos,limit,maxdepth,PATH,decisioncount):
        if depth>=maxdepth[0]:
            maxdepth[0] = depth
            print depth,decisioncount,PATH
        c = ClassMap[rank]
        pos +=1
        if Classes[c]<0:
            if depth >=838:
                print Classes
            Classes[c]=rank
            if pos==limit:
                btDecision(rankmap[rank][swaptype*2+depth%2],depth+1,Classes,ClassMap,rankmap,swaptype,maxdepth,PATH+[swaptype],decisioncount+1)
            else:
                pos = monoTrack(rankmap[rank][swaptype*2+depth%2],depth+1,Classes,ClassMap,rankmap,swaptype,pos,limit,maxdepth,PATH+[swaptype],decisioncount)
            Classes[c]=-1
        return pos
    
    def btDecision(rank,depth,Classes,ClassMap,rankmap,lastswap,maxdepth,PATH,decisioncount):
        if lastswap==0:
            limit = 14
            swaptype = 1
        else:
            limit = 10
            swaptype = 0
        if swaptype==1:
            monoTrack(rank,depth,Classes,ClassMap,rankmap,swaptype,0,1,maxdepth,PATH,decisioncount)
        else:    
            limit = monoTrack(rank,depth,Classes,ClassMap,rankmap,swaptype,0,limit,maxdepth,PATH,decisioncount)
            for swaplen in reversed(range(1,limit)):
                monoTrack(rank,depth,Classes,ClassMap,rankmap,swaptype,0,swaplen,maxdepth,PATH,decisioncount)
    
    
    #btDecision(0,0,[-1]*840,ClassMap,rankmap,1,[0],[],0)
    
    Classes2 = []*840
    for i in range(840):
        Classes2.append([[],[],[]])
    for r in range(5040):
        for j in [0,2]:
            r2 = rankmap[r][j]
            Classes2[ClassMap[r2]][j].append(ClassMap[r])
    
    Classes = []
    for i in range(840):
        Classes.append([])
    for i in range(5040):
        Classes[ClassMap[i]].append(i)
    
    Classes3=[]
    for i in range(5040):
        Classes3.append([])
    for i in range(5040):
        for j in range(4):
            Classes3[rankmap[i][j]].append((j, i, ClassMap[i]))
            Classes3[rankmap[i][j]].sort()

    #for i in Classes[ClassMap[5039]]:
        #print i,ClassMap[i], (ClassMap[rankmap[i][0]], rankmap[i][0]), (ClassMap[rankmap[i][1]], rankmap[i][1]), (ClassMap[rankmap[i][2]], rankmap[i][2]), (ClassMap[rankmap[i][3]], rankmap[i][3]), Classes[ClassMap[i]], Classes3[i]
        #print i, Classes3[i]
        #for (j,r) in Classes3[i]:
            #print r, ClassMap[r],Classes[ClassMap[r]]

    for r in Classes[1]:
        Q = [r]
        for i in range(5):
            Q2 = []
            for q in Q:
                for (type,links, c) in Classes3[q]:
                    if type in [0,2]:
                        Q2 += [links]
            Q = Q2
            Q2 = list(set(Q2))
            Q2.sort()
            print Q2
        
        
        
            
            
    '''        
    #EVOLUTIONARY
    maxsofar = 0
    p1 = [1]*840
    p2 = [0]*840
    weight = [0]*840
    maxweight = 0
    maxp1 = 0
    maxp2 = 0
    while True:
        c=[]
        L = []
        for i in range(5):
            for i,x in enumerate(p1):
                if x==1:
                    weight[i]+=1
                else:
                    weight[i]-=1
                rand = random.random()
                if rand<0.15:
                    c.append(p1[i])      
                elif rand < 0.3:
                    c.append(p2[i]) 
                else:
                    c.append(random.randint(0,1))               

            try:
                backtrackSEQ(0,0,[-1]*840,ClassMap,rankmap,c,0,[0],[],[0],[])
            except MyError,e:
                x = []
                x.extend(c)
                L.append((e,x))
        for (e,c) in L:
            if e.max > maxp2:
                if e.max > maxp1:
                    p1,p2 = c,p1
                    maxp1,maxp2 = e.max,maxp1
                else:
                    p2 = c
                    maxp2 = e.max
                print e.max, c
                print e.PATH
                print weight
    '''
    '''
        #EVOLUTIONARY
    maxsofar = 0
    p1 = [1]*840
    p2 = [0, 0, 0, 0, 0, 0, 0, 1]*105
    weight = [0]*840
    maxweight = 0
    maxp1 = 0
    maxp2 = 0
    while True:
        L = []
        for i in range(1):
            c=[]
            for i,x in enumerate(p1):
                if x==1:
                    weight[i]+=1
                else:
                    weight[i]-=1
                rand = random.random()
                if rand<0.499:
                    c.append(p1[i])      
                elif rand < 0.998:
                    c.append(p2[i]) 
                else:
                    c.append(random.randint(0,1))               
            d= track(0,0,[-1]*840,ClassMap,rankmap,c)
            L.append((d,c))
        for (d,c) in L:
            if d>maxp2:
                if d>maxp1:
                    p2 = []
                    p2.extend(p1)
                    p1=[]
                    p1.extend(c)
                    maxp1,maxp2 = d,maxp1
                else:
                    p2=[]
                    p2.extend(c)
                    maxp2 = d
                print d, c
    '''
    '''   
    dmax = 0
    SEQ = []
    while True:
        d0 =track(0,0,[-1]*840,ClassMap,rankmap,SEQ+[0])
        d1 =track(0,0,[-1]*840,ClassMap,rankmap,SEQ+[1])
        
        if d0>=d1:
            d = d0
            SEQ +=[0]
        else:
            d = d1
            SEQ +=[1]
        
        if d>=dmax:
            dmax=d
            print d, SEQ
        '''
    '''
        for i,x in enumerate(SEQ):
            SEQ[i]=0
            d0 =track(0,0,[-1]*840,ClassMap,rankmap,SEQ)
            SEQ[i]=1
            d1 =track(0,0,[-1]*840,ClassMap,rankmap,SEQ)
            
            if d0>d1:
                d = d0
                SEQ[i]=0
            else:
                d= d1
                SEQ[i]=1
            if d>=dmax:
                dmax=d
                print d,SEQ
        '''    
    '''
    f = open('out.txt','w')
    C0 = []
    for r in range(5040):
        C = []
        parity = 0
        r5=r
        r7=r
        while ClassMap[r7] not in C:
            C += [ClassMap[r7]]
            r5 = rankmap[r5][1]
            r7 = rankmap[r7][3]
            
            parity = (parity+1)%2
        #print >>f, r, C
        C0 += [C]
        MAX = len(C)
   ''' 
    '''
    FFF = []
    for i,C in enumerate(C0):
        FF = []
        FF.extend(C)
        for r,C2 in enumerate(C0):
            for x in C2:
                if x in C and ClassMap[r] not in FF:
                    FF +=[ClassMap[r]]
                    print C, C2
        FFF +=[FF]
        print FF
    '''    
    
    '''
    for i in range(5040):
        c = ClassMap[i]
        for r,C in enumerate(C0):
                
            
        RANGES[i] = 
    '''
    ''' 
    for j,C in enumerate(C0):
        for k,D in enumerate(C0):
            match = False
            for i,r in enumerate(C):
                if r in D:
                    print >>f,j,k,i
                    match = True
                    break
    '''
            #if not match:
                #print >>f,j,k,-1
            
    
    
    print "done"
    #print SW
    #for i in range(5040):
    #    print SWAPS2[i]
        


#MAIN    
if __name__ == "__main__":
    freeze_support()
    main()