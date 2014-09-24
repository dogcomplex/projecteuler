'''
Created on Apr 27, 2014

@author: W
'''

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
 
RADref = {}
Rads = {}

Rads[1] = [[1],[1]]
Rads[2] = [[2],[2]]

RADref[1]=1
RADref[2]=2

 
def rad(n):
    if n == 1:
        return 1, [1]

    i=0
    while P[i]<=n:
        if n%P[i]==0:
            if RADref.has_key(P[i]) and RADref.has_key(n/P[i]) and RADref[P[i]] == RADref[n/P[i]]:
                Rads[RADref[P[i]]][1] += [n]
                RADref[n] = RADref[P[i]]
            else:
                L = Rads[RADref[P[i]]][0] + Rads[RADref[n/P[i]]][0]
                L = list(set(L))
                r=1
                for i in L:
                    r*=i
                if Rads.has_key(r):
                    Rads[r][1] += [n]
                    RADref[n] = r
                else:
                    Rads[r] = [L,[n]]
                    RADref[n] = r
            break
        i +=1

    



for p in range(1,100001):
    if isprime(p):
        P += [p]
        Rads[p] = [[p],[p]]
        RADref[p] = p
    else:
        rad(p)


K = Rads.keys()
K.sort()
i = 10000
for k in K:
    l = len(Rads[k][1])
    if i-l <= 0:
        print "here", k,i,l,Rads[k], Rads[k][1][i-1]
        break
    i -= l
    if i >= 0:
        print k, i, l, Rads[k]

    
    
    