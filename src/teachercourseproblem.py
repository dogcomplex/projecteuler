'''
Created on Mar 5, 2012

@author: W
'''
from random import *

P = []
n = 5
for i in range(n):
    P.append([])
    for j in range(n):
        P[i].append([random()])
    
    
PMAX = []    
for i in range(n):
    pmax = 0
    jmax = 0
    for j in range(n):
        if P[i][j]>pmax:
            pmax = P[i][j]
            jmax = j    
    PMAX += [(pmax,i,jmax)]
    
PMAX.sort(reverse=True)
print PMAX

COURSELIMIT = 4
coursepicks = [-1]*n
for i in PMAX:
    if coursepicks[PMAX[i][2]]==-1:
        coursepicks[PMAX[i][2]] = PMAX[i][1]
    else:
        for ii in range(n):
            

print coursepicks