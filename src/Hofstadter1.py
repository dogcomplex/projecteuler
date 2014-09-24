'''
Created on 2010-05-03

@author: Warren
'''
Q = {}
Q[1]=1
N = 10000
M = {}
M[1]=0
P = {}
P[1]=0
maxM = 0
maxP = 0
maxS = 0
for n in range(2, 1000000):
    a1 = n-Q[n-1]
    a2 = n-Q[n-2]
    M[n] = 1+M[a1]
    P[n] = 1+P[a2]
    Q[n] = Q[a1] + Q[a2]
    maxM = max(M[n],maxM)
    maxp = max(P[n],maxP)
    maxS = max(M[n]+P[n],maxS)