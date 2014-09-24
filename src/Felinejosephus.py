'''
Created on Jun 30, 2010

@author: Warren
'''
def gcd(a, b):
    if a > b: a, b = b, a
    while a > 0: a, b = (b % a), a
    return b

lcm = lambda a, b: a * b / gcd(a, b)


def jos(n,k,l):
    Hitseq = []
    L = []
    for i in range(n):
        L.append([i,l])
    pos = (k-1)%n
    while L:
        hit = L[pos][0]
        if L[pos][1] == 1:
            L.remove(L[pos])
            n -=1
            pos -=1
        else:
            L[pos][1] -=1
        Hitseq += [hit+1]
        pos += k
        if n>0:
            pos %=n
    return Hitseq

def josInvincible2(n,k,l):
    L = []
    N = n
    for i in range(n):
        L.append([i,l])
    pos = (k-1)%n
    S = set([])
    while len(S)<N:
        S.add(L[pos][0])
        if L[pos][1] == 1:
            L.remove(L[pos])
            n -=1
            pos -=1
            if len(L)==1:
                if L[0][1]==l:
                    return L[0][0]+1
                else:
                    return False
        else:
            L[pos][1] -=1
        pos += k
        pos %=n
    return False

'''  
def josRounds(n,k,l):
    r=1
    ret = []
    Elem = list(range(n))
    L = [l]*n
    minS = l
    pos = 0
    T = []
    while r<n:
        k2 = k% (n-r+1)
        firstpass = True
        start = pos
        S = []
        T = []
        minS = l
        while True:
            pos += k2
            pos %= n-r+1
            x = Elem[pos]
            if firstpass:
                S += [x]
                L[x]-=1
                if L[x] < minS:
                    minS = L[x]
                if L[x]==0:
                    break
            else:
                T +=[x]
                L[x]-=1
                if L[x]==minS-1:
                    break
                
            if start==pos:
                firstpass=False
        if not firstpass:
            h = -1 + minS
            for y in S:
                L[y] -=h 
        Elem.remove(x)
        pos -=1
        r+=1
        pos %= n-r+1
        if h>0:
            ret += [(S,h+1)]
        if T:
            ret.extend(T)
        #print r,n, pos, x, k2, S, h, T, minS, L
    return ret
'''
        
def josInvincible(n,k,l):
    r=1
    Elem = list(range(n))
    L = [l]*n
    minS = l
    pos = 0
    SET = set([])
    T = []
    while r<n:
        k2 = k% (n-r+1)
        firstpass = True
        start = pos
        S = []
        T = []
        minS = l
        while True:
            pos += k2
            pos %= n-r+1
            x = Elem[pos]
            if firstpass:
                S += [x]
                L[x]-=1
                if L[x] < minS:
                    minS = L[x]
                if L[x]==0:
                    break
            else:
                T +=[x]
                L[x]-=1
                if L[x]==minS-1:
                    break
                
            if start==pos:
                firstpass=False
                
        #end premature if not invincible
        SET.union(set(S))
        if len(SET)==n:
            return False
        
        if not firstpass:
            h = -1 + minS
            for y in S:
                L[y] -=h 
        Elem.remove(x)
        pos -=1
        r+=1
        pos %= n-r+1
        #print r,n, pos, x, k2, S, h, T, minS, L
    for i,x in enumerate(L):
        if x==l:
            return ((i-1)%n)+1
    return False


def alLCM(n):
    x = 2
    for i in range(3,n+1):
        x = lcm(x,i)
    return x

def createK(Hist):
    n= len(Hist)+1
    lc = alLCM(n)
    L = list(range(Hist[0],lc,n))
    for i,x in enumerate(Hist[1:]):
        #print n-i-1,x, L, Hist
        L = [y for y in L if y%(n-i-1)==x]
    if L:
        return L[0]
    else:
        return -1
        

def josBacktrack(pos,L2,Elem,l,Hist):
    n=len(Elem)
    N=len(L2)
    POS = pos
    if n==1 and L2[Elem[0]]==l:
        k = createK(Hist)
        if k>=0:
            print N, L2, Hist, k, alLCM(N)
    
    for k2 in range(n):
        L = []
        L.extend(L2)
        pos = POS
        firstpass=True
        S =[]
        T =[]
        minS = l
        start = pos
        while True:
            pos += k2
            pos %= n
            x = Elem[pos]
            if firstpass:
                S += [x]
                L[x]-=1
                if L[x] < minS:
                    minS = L[x]
                if L[x]==0:
                    break
            else:
                T +=[x]
                L[x]-=1
                if L[x]==minS-1:
                    break
                
            if start==pos:
                firstpass=False
        
        invincible = False
        pure=True
        for y in L:
            if y==l:
                invincible=True
            elif y>0:
                pure=False
        if not invincible:
            continue
        #if pure and n>3:
        #    print N, L2, Hist, n
        #    continue
        
        if not firstpass:
            h = -1 + minS
            for y in S:
                L[y] -=h 
        i = Elem.index(x)
        josBacktrack((pos-1)%(n-1) , L, Elem[:i]+Elem[i+1:], l, Hist+[k2] )
        
    

def josRounds(n,k,l):
    r=1
    Elem = list(range(n))
    L = [l]*n
    minS = l
    pos = 0
    SET = set([])
    T = []
    ret = []
    CASE2 = False
    specs = []
    specs2 = []
    while r<n:
        k2 = k%(n-r+1)
        firstpass = True
        start = pos
        S = []
        T = []
        minS = l
        while True:
            pos += k2
            pos %= n-r+1
            x = Elem[pos]
            if firstpass:
                S += [x]
                L[x]-=1
                if L[x] < minS:
                    minS = L[x]
                if L[x]==0:
                    break
            else:
                T +=[x]
                L[x]-=1
                if L[x]==minS-1:
                    break
                
            if start==pos:
                firstpass=False
                
        #end premature if not invincible
        SET.union(set(S))
        if len(SET)==n:
            return False,[], CASE2, []
        
        h = -1 + minS
        if not T:
            CASE2 = r
            specs2 += [(S,1)]
            specs += [(len(S),1)]
        else :
            specs2 += [(S,h+1,T)]
            specs += [(len(S),h)]
        if not firstpass:
            
            for y in S:
                L[y] -=h 
            ret += [(S,h+1)]
            S = T
        ret += [S]
        Elem.remove(x)
        pos -=1
        r+=1
        pos %= n-r+1
        #print r,n, pos, x, k2, S, h, T, minS, L
    for i,x in enumerate(L):
        if x==l:
            return ((i-1)%n)+1, ret, CASE2, specs, specs2
    return False, ret, CASE2, specs, specs2
       

def invincible(seq,l):
    ''' 
    x = seq[-l]
    for y in seq[-l:]:
        if y !=x:
            return False
    return x
    ''' 
    x = seq[-l]
    if seq[-l:] == [x]*l:
        return x
    else:
        return False

def findJosephus(maxn,file):
    ret = []
    LCM = 2
    for n in range(2,30):
        LCM = lcm(LCM,n)
        GCD = 0
        GCD2 = 0
        count = 0
        for k in range(n,LCM+1,n):
            #x = josInvincible2(n,k,n*2)
            x,R,case2,specs,specs2 = josRounds(n,k,n*2)
            #x = invincible(seq,n*2)
            X = []
            for i in reversed(range(2,n+1)):
                X += [k%i]
            
            if x:
                #print >>file, X
                print >>file,n,k
                #print n, k, x
                if k%2==0:
                    if GCD:
                        GCD = gcd(k,GCD)
                    else:
                        GCD = k
                else:
                    count+=1
                    if GCD2:
                        GCD2 = gcd(k,GCD2)
                    else:
                        GCD2 = k
                    #print n,k,x,LCM,GCD2,count
        print n,GCD, GCD2
    return ret



def getBounds(n,k,l):
    r=1
    Elem = list(range(n))
    L = [l]*n
    minS = l
    pos = 0
    SET = set([])
    T = []
    count = 0
    while r<n:
        k2 = k% (n-r+1)
        firstpass = True
        start = pos
        S = []
        T = []
        minS = l
        count1 = 0
        count2 =0
        while True:
            pos += k2
            pos %= n-r+1
            x = Elem[pos]
            if firstpass:
                S += [x]
                L[x]-=1
                if L[x] < minS:
                    minS = L[x]
                if L[x]==0:
                    break
                count1 +=1
            else:
                T +=[x]
                L[x]-=1
                count2 +=1
                if L[x]==minS-1:
                    break
                
            if start==pos:
                firstpass=False
        
        if not firstpass:
            h = -1 + minS
            for y in S:
                L[y] -=h 
        else:
            h=0
        count += count1*h + count2
        if count == l-n:
            return 0
        Elem.remove(x)
        pos -=1
        r+=1
        pos %= n-r+1
        #print r,n, pos, x, k2, S, h, T, minS, L
    #print L
    for i,x in enumerate(L):
        if x > 0:
            if x > n:
                return l-x+1
            return 0
    
def findBounds(maxn,file):
    ret = []
    LCM = 2
    for n in [3,5,7,11,13,17,19,23,31]:
        LCM = lcm(LCM,n)
        lbound = 0
        for k in range(n,LCM+1,n):
            x = getBounds(n,k,n*2)
            R = josRounds(n,k,n*2)
            if x:
                print >>file,n,k,x, k/n
            if x > lbound:
                lbound = x
                print n,k,x, LCM, R
        print n, lbound
        ret += [lbound]
    return ret    

def step(L,X,pos,k):
    S = []
    n = len(X)
    minL = 99999999
    firstpass = True
    while True:
        pos = (pos+k)%n
        x = X[pos]
        if S and x==S[0]:
            break
        S += [x]
        if L[x]<minL:
            minL = L[x]
        
def backtrackGen(limit):
    for n in range(2,limit):
        l = 2*n
        josBacktrack(0,[l]*n,list(range(n)),l,[])
    
def breakK(k,N):
    L = []
    for i in reversed(range(2,N+1)):
        L += [k%i]
    return L
    
def grow(N,L,LCMS):
    if N>20:
        return
    LCMS[N] = lcm(LCMS[N-1],N)
    L2 = []
    backlinks = {}
    countbreaks = 0
    for (n,k) in L:
        nomatch = True
        for k2 in range(k,LCMS[N],LCMS[n]):
            if josInvincible2(N,k2,N*2):
                L2 += [(N,k2)]
                backlinks[(N,k2)]=(n,k)
                nomatch = False
            #else:
                #print breakK(k2,N)
                print k,N, k2, breakK(k2,N)
        if nomatch and n==N-1:
            countbreaks+=1
            #if gcd(N,k)!=1:
            #print (n,k), k%N
            #for k2 in range(k,LCMS[N],LCMS[n]):
            #    print breakK(k2,N)
    #print countbreaks
    L2 = list(set(L2))
    L2.sort()
    print N, len(L2), LCMS[N], L2
    #print backlinks
    grow(N+1,L2,LCMS)

if __name__ == "__main__":   
    file = open('out.txt','w')
    
    #backtrackGen(10)
    findJosephus(20,file)
    LCMS = {}
    LCMS[1]=1
    
    #grow(2,[(1,0)],LCMS)
    