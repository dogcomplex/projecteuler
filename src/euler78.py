'''
Created on May 4, 2014

@author: W
'''

P = {}

def p(n,m):
    if n==m:
        if P.has_key((n,m-1)):
            return 1 + P[(n,m-1)]
        return 1 + p(n,m-1)
    if m==0 or n<0:
        return 0
    if n==0 or m==1:
        return 1
    s = 0
    if P.has_key((n-m,m)):
        s += P[(n-m,m)]
    else:
        P[(n-m,m)] = p(n-m,m)
        s += P[(n-m,m)]
    
    if P.has_key((n,m-1)):
        s += P[(n,m-1)]
    else:
        P[(n,m-1)] = p(n,m-1)
        s += P[(n,m-1)]
    
    return s

import sys
sys.setrecursionlimit(1500)
for k in range(1,1000):
    y = p(5*k+4,5*k+4)
    print k,  5*k+4, y
    if y%1000000==0:
        break