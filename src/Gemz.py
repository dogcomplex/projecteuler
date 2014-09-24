'''
Warren Koch
V00482478
Jan 28, 2010
'''

import random,math

gems = {'R':5,
         'D':10,
         'E':4,
         'S':6
         }

'''
Generates a text-based table with the required frequencies
'''
def genTable(N,M):
    s = ""
    for i in range(N):
        for i in range(M):
            elem = 'X'
            r = random.random()
            if r<0.05:
                elem = 'D'
            elif r<0.15:
                elem = 'R'
            elif r<0.25:
                elem = 'E'
            elif r<0.3:
                elem = 'S'
            s +=elem
        s +='\n'
    return s

'''
Generates dictionaries of vertices and edges with weight according to type of gem in s.
'''
def graphicize(s,N,M):
    global V,E
    i=0
    for c in s:
        if c !='\n':
            if c !='X':
                E[i] = []
                V[i] = gems[c]
                if i%M > 0 and i-1 in V:
                        E[i-1]= E.get(i-1,[]) + [i]
                        E[i]= E.get(i,[]) + [i-1]
                    
                if i >= M and i-M in V:
                        E[i-M]= E.get(i-M,[]) + [i]
                        E[i]= E.get(i,[]) + [i-M]
                  
            i+=1

''' 
Visits each unvisited vertex in W, searching for the best path. Recursively determines the best path from each vertex,
 and then returns that path's loot + the vertex's value
'''
def dfs(W,visited):
    global V,E
    max=0
    maxVisited ={}
    for v in W:
        if v not in visited:
            visited[v]=True
            x,visits = dfs(E[v],visited)
            x += V[v]
            visited.pop(v)
            if x > max:
                max = x
                maxVisited = visits
    visited.update(maxVisited)
    return max, visited


'''
MAIN
'''
N=16
M=16
for i in range(10):
    s = genTable(N,M)
    print(s)
    V={}
    E={}
    graphicize(s,N,M)
    max,best = dfs(list(V.keys()),{})
    print "Answer: ", max
    print


    
