'''
Created on Apr 30, 2014

@author: W
'''
'''
Created on 2011-04-13

@author: Warren
'''
from math import *

P = [2,3,5]

def isprime(p):
    if p<=1:
        return False
    for i in range(2,int(sqrt(p))+1):
        if p%i==0:
            return False
    return True

def nextprime(p,P):
    p +=2
    i = 0
    while True:
        if not isprime(p):
            p +=2
        else:
            P += [p]
            return p

def comp(p,p2,diff):
    if p==p2:
        return False
    p = str(p)
    p2 = str(p2)
    if len(p)!=len(p2):
        return False
    POS = []
    for i in range(len(p)):
        if p[i]!=p2[i]:
            if diff==-1 or diff==(p[i]+p2[i]):
                diff = p[i]+p2[i]
                POS+=[i]
            else:
                return False
    return POS

def tryswap(p,POS):
    start = 0
    if 0 in POS:
        start = 1
    c = 0
    p = list(str(p))
    for d in range(start,10):
        for j in POS:
            p[j]=str(d)
        if isprime(int(''.join(p))):
            c +=1
    return c


'''            
Sets = {}

p=5
D = [0]
i=0
C = [0,0,0]
while p < 100000:
    p = nextprime(p,P)
    if len(str(p)) > len(D):
        D += [i]
        
    c = 1
    L = [p]
    
    for q in P[D[-1]:]:
        POS = comp(p,q,-1)
        if POS:
            ttt= tryswap(p,POS)
            if ttt >=7:
                print p,q,POS, ttt
                
                

    i +=1
'''

def tryit(pre,k,star): 

    if k==0:
        for i in range(0,10):
            if pre.find('*'):
                L = []
                c =0
                for d in range(0,10):
                    if d==0 and pre[0]=='*':
                        continue
                    s = pre.replace('*', str(d))
                    if isprime(int(s)):
                        c+=1
                        L+=[int(s)]
                if c>=7:
                    print 'THIS', pre, c, L
        #print pre,k  
    else:
        if k!=1 or star==1:
            for i in range(0,10):
                tryit(pre+str(i),k-1,star)         
        tryit(pre+'*',k-1,1) 
           
            
for k in range(7,8):      
    for i in range(1,10):
        tryit(str(i),k,0)            
    tryit('*',k,1)    
            
        