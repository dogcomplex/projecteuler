P = []

import math
def isprime(p):
    if p==1:
        return False
    if p%2==0 and p!=2:
        return False
    for i in range(2,int(math.sqrt(p))+1):
        if p%i==0:
            return False
    return True

def tryp(i,n,k,L,printtog):
    #print P[i], i, n, k, L
    while n>=2 and i>=0:
        if P[i]<=n and P[i]<=k:
            tryp(i,n-P[i],P[i],L+[P[i]],printtog)
        i-=1
        #print '-', i,n,k,L
    if n==0:
        C[0]+=1
        if printtog:
            print L, C[0]

for n in range(2,1000):
    if isprime(n):
        P += [n]
    i = len(P)-1
    C = [0]
    L = []
    tryp(i,n,n,[],0)
    print n,C[0]
    if C[0]>5000:
        #tryp(i,n,n,[],1)
        break
        
