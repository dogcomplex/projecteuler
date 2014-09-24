'''
Created on Nov 16, 2011

@author: W
'''
class graph:
    n = 0
    S = {}
    Z = {}
    E = {}
    oldS = {}
    
def addedge(G,vi,vj,directed=0):
    G.E[vi].add(vj)
    if not directed:
        G.E[vj].add(vi)
        
def addvert(G,name,val):
    
    G.S[name] = val
    G.Z[name] = val
    G.E[name] = set([])
    G.n +=1

def updateZ(G,vi):
    z = G.S[vi]
    W = 1
    m = len(G.E[vi])
    for vj in G.E[vi]:
        z += G.Z[vj]
        W += 1
    G.Z[vi]=z/W

def nextstep(G):
    newE = {}
    newS = {}
    newZ = {}
    for (vi,zi) in G.Z.items():
        newE[vi] = set([])
        newS[vi] = zi
        newZ[vi] = zi
    
    for (vi,zi) in G.Z.items():
        for wi in G.E[vi]:
            if wi != vi:
                for wwi in G.E[wi]:
                    if wwi != vi:
                        newE[vi].add(wwi)         
                        newE[wwi].add(vi)  
    G.oldS = G.S
    G.oldE = G.E
    G.E = newE
    G.S = newS
    G.Z = newZ
    
def cost(G):
    sum = 0
    for i in G.S.keys():
        sum += (G.S[i]-G.Z[i])**2
        for j in G.E[i]:
            sum += (G.Z[i]-G.Z[j])**2
    return sum

G = graph
V = [0,0.1,1]
addvert(G,V[0],V[0])
addvert(G,V[1],V[1])
addvert(G,V[2],V[2])
addedge(G,V[0],V[1])
addedge(G,V[1],V[2])
addedge(G,V[0],V[2])

print G.E, G.S
for i in range(20):
    for v in V:
        updateZ(G,v)
        print G.Z


sum = 0
avg = 0
avgS = 0
for i in G.S.keys():
    sum += (G.S[i]-G.Z[i])**2
    avg += G.Z[i]
    avgS += G.S[i]
print '1 iteration, cost per node (regret)', sum, avg/G.n, avgS/G.n


nextstep(G)

print G.E, G.S
for i in range(10):
    for v in V:
        updateZ(G,v)
        print G.Z
      

print '2 iterations, total cost vs last rounds Z', cost(G)
sum = 0
for i in G.S.keys():
    sum += (G.S[i]-G.Z[i])**2
print 'cost per node',sum

G.S = G.oldS
print 'cost per old S', cost(G)
G.E = G.oldE
print 'cost per old Edges and S', cost(G)

sum = 0
for i in G.S.keys():
    sum += (G.S[i]-G.Z[i])**2
print 'cost per node',sum

print G.Z[V[0]]-G.Z[V[2]], G.Z[V[0]]-G.Z[V[1]],G.Z[V[2]]-G.Z[V[1]], (G.Z[V[0]]-G.Z[V[1]])/(G.Z[V[2]]-G.Z[V[1]])

