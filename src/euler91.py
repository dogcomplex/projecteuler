'''
Created on Oct 4, 2012

@author: W
'''

n=50
T = []
for i in range(n+1):
    for j in range(n+1):
        T += [(i,j)]
T.remove((0,0))

def alph((x,y),(u,v)):
    if x<u:
        return (x,y),(u,v)
    elif x==u:
        if y<=v:
            return (x,y),(u,v)
        else:
            return (u,v),(x,y)
    else:
        return (u,v),(x,y)

def sanity((x,y),(u,v)):
    if (x,y)==(u,v):
        return False
    a2 = x*x + y*y
    b2 = u*u + v*v
    c2 = (x-u)**2 + (y-v)**2
    if a2 + b2 == c2:
        return True
    elif a2 + c2 == b2:
        return True
    elif b2 + c2 == a2:
        return True
    return False

S = []
for x,y in T:
    for u,v in T:
        if sanity((x,y),(u,v)):
            S += [((x,y),(u,v))]
            

print len(S), S
