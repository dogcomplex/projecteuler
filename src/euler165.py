'''
Created on May 14, 2013

@author: W
'''

N = 20000
S = [290797]
for i in range(1,N):
    S += [(S[i-1]*S[i-1])%50515093]

T = []
for s in S:
    T += [s%500]

P = []
for i in range(N/2):
    P += [(int(T[2*i]),int(T[2*i+1]))]

L = []
for i in range(N/4):
    if P[2*i][0] < P[2*i+1][0]:
        L +=[(P[2*i],P[2*i+1])]
    else:
        L +=[(P[2*i+1],P[2*i])]



L.sort(key=lambda (a,b): a[0])

SWEEP = []
r = 0
s = 0
for (a,b) in L:
    if a[0] > s:
        s = a[0]
    
class node:
    def __init__(self,v):
        self.v = v
        self.left = None
        self.right = None

    
class bintree:
    def __init__(self):
        self.root = None
        
    def add(self,root,v):
        if root:
            root = node(v)
        else:
            if v < root.v:
                root.left = self.add(root.left,v)
            else:
                root.right = self.add(root.right,v)
        return root
                 
    def left(self,root,n):
    
    