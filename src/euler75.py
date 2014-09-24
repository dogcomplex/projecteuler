'''
Created on May 6, 2014

@author: W
'''
'''
from math import *
from collections import *
L = OrderedDict()
T = 15000

for b in xrange(1,T/2):
    for a in xrange(1,b+1):
        if a+2*b>T:
            break
        c = sqrt(a**2 + b**2)
        if c ==int(c):
            c = int(c)
            s = a+b+c
            if s<= T:
                if L.has_key(s):
                    L[s] += [(a,b,c)]
                else:
                    L[s] = [(a,b,c)]
            else:
                break
        
    

print L
for k in sorted(L.keys()):
    if len(L[k])>1:
        print k,L[k]
print len(L)

'''
from math import *

def isprime(n):
    if n<=1:
        return False
    if n!=2 and n%2==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

PrimeTriangles = {}


ANS = {}
T = 1500


P = []
for n in range(2,T):
    if isprime(n):
        P +=[n]
print P

SQ = [2]
for c in range(3,T/2+1):
    SQ += [c*c]
    bi = 0
    b2 = 0
    c2 = c*c
    
    while bi < len(SQ):
        b2 = SQ[bi]
        bi+=1
        a2 = c2-b2
        if b2 > a2:
            # oops.  c >= a >=b
            break
        a = sqrt(a2)
        if a==int(a) and a>=1:
            a = int(a)
            b = int(sqrt(b2))
            t = a+b+c
            if t<=T:
                if ANS.has_key(t):
                    # more than 1 answer
                    ANS[t] += [(b,a,c)]  
                else:
                    ANS[t] = [(b,a,c)]  
                #print t,(c,a,b),(c2,a2,b2)          
            else:
                break
            
        
        
        
print ANS
count = 0
for k in ANS.keys():
    if len(ANS[k])==1:
        count +=1
print ANS[120]
print count
