'''
Created on 2011-04-13

@author: Warren
'''
from math import *

def rootseq(n):
    a = int(sqrt(n))
    L = []
    b = 1
    c = a
    wrap = -1
    while wrap < 0 and not(a==0 or b==0 or c==0):
        L +=[(a,b,c)]
        b = int((n - c**2)/b)
        if b==0:
            L = []
            break
        a = int((sqrt(n)+c)/b)
        c = -int(c-a*b)
        for i,x in enumerate(L):
            if x == (a,b,c):
                wrap = i
    return L,wrap          

''' 64'''
'''
count = 0
for i in range(2,10000+1):
    L,wrap =rootseq(i)
    #print i,L,len(L[wrap:])
    if len(L[wrap:])%2==1:
        count +=1
print count
'''


