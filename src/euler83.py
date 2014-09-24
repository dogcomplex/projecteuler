'''
Created on May 4, 2014

@author: W
'''
from heapq import *



def shortestpath(D,E,Path):
    while D:
        (du,u) = min(D.values())
        D.pop(u) 
        for (wv,v) in E[u]:
            if D.has_key(v):
                if du + wv < D[v][0]:
                    D[v] = (du + wv,v)
                    Path[v]=(u,du + wv)
                    if v==1:
                        print D[v],du,u,wv,v
        if u==80*80-1:
            print u, du
            
                 
             
    

V = [] 
i = 0                
f =  open('matrix.txt', 'r')
line = "first"
while line != '':
    line = f.readline()
    V += line[:-1].split(',')
    i+=1
V = V[:-1]
f.closed  
  
i = 0    
while i < 80*80:
    V[i]=int(V[i])
    i +=1
             
E = {}
for i in range(80*80):
    E[i]=[]


INF = 100000000
i = 80   
#UP/DOWN 
while i < 80*80:
    E[i]+=[(V[i-80],i-80)]
    E[i-80]+=[(V[i],i)]
    i +=1

i = 1
#left/right
while i < 80*80:
    if i%80!=0:
        E[i]+=[(V[i-1],i-1)]
        E[i-1]+=[(V[i],i)]
    i +=1

D = {}
for i in range(80*80):
    D[i] = (INF,V[i])
D[-1]= (0,-1)
E[-1]= [(V[0],0)]

Path = {}
shortestpath(D,E,Path)

u = 80*80-1
while Path.has_key(u):
    u,du = Path[u]
    
    print u,du, E[u]
    
print D
# for each vertex, D[v]=inf, D[start]=0             
