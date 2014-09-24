'''
Created on May 27, 2014

@author: W
'''

import math




def shrink(L):
    return int(''.join(map(str,L)))

def unzip(n):
    L = str(n).split()
    map(int,L)
    return L

def isprime(n):
    if n==2:
        return True
    if n%2==0 or n<=1:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True


def permute(n,L):
    if n==0:
        if isprime(shrink(L)):
            return [shrink(L)]
    else:
        S = []
        for i in range(0,n):
            s = permute(n-1,L)
            if s:
                S += s
            if n%2==1:
                temp = L[0]
                L[0]=L[n-1]
                L[n-1]=temp
            else:
                temp = L[i]
                L[i] = L[n-1]
                L[n-1] = temp
        return S
    
    
L = list(range(1,10))
#permute(len(L),L)

PrimeSets = {}

def choose(L,k,P):
    if k==0:
        #print P
        S= permute(len(P),P)
        if S:
            P.sort()
            print P
            PrimeSets[tuple(P)]= S
                
    for i in range(len(L)):
        if not P or L[i]>P[-1]:
            choose(L[i+1:],k-1,P+[L[i]])

# there is no 9 digit prime with 1 to 9
for i in range(1,9):            
    choose(L,i,[])
    

    
def combine(S,P,Keys,k,tally):
    if not S:
        print P,tally
        for ps in P:
            print len(ps),
        print
        TALLY[0] += tally
        return 1
    count = 0
    for i in range(k,len(Keys)):
        ps = Keys[i]
        s = set(ps)
        if s.issubset(S):
            count += len(PrimeSets[ps])* combine(S.difference(s),P+[ps],Keys,i+1,tally*len(PrimeSets[ps]))
    return count
                
K = PrimeSets.keys()
K.sort()  
   
TALLY = [0]           
print combine(set(range(1,10)),[],K,0,1)

print TALLY
'''
print PrimeSets[(1,4,6)]
for ps in PrimeSets:
    for s in PrimeSets[ps]:
        if not isprime(s):
            print 'wtf', ps,s
'''