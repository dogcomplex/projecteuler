'''
Created on Jul 4, 2013

@author: W
'''
FACT = [1,1,2,6,24,120,720,5040,40320,362880]

def f(n):
    s = str(n)
    F = 0
    for d in s:
        F += FACT[int(d)]
    return F
        
def s(n):
    s = str(n)
    SF = 0
    for d in s:
        SF += int(d)
    return SF

G = {}

for n in range(1,100000):
    i = s(f(n))
    if G.has_key(i):
        G[i] += [n]
    else:
        G[i] = [n]
    
print G
S = 0
for i in G.keys():
    S += s(min(G[i]))
    print i, min(G[i]), len(G[i]), s(min(G[i])), S