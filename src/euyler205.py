'''
Created on Apr 27, 2014

@author: W
'''
from distutils.msvc9compiler import WINSDK_BASE

EQ = []
GT = []
LT = []
for i in range(37):
    EQ += [0]
    GT += [0]
    LT += [0]

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                for e in range(1,5):
                    for f in range(1,5):
                        for g in range(1,5):
                            for h in range(1,5):
                                for i in range(1,5):
                                    EQ[a+b+c+d+e+f+g+h+i] +=1

total = sum(EQ)
t = total
less = 0

for i in range(37):
    t -= EQ[i]
    GT[i] = t
    LT[i] = less
    less += EQ[i]

    

EQ2 = []
GT2 = []
LT2 = []
for i in range(37):
    EQ2 += [0]
    GT2 += [0]
    LT2 += [0]

for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                        EQ2[a+b+c+d+e+f] +=1

total2 = sum(EQ2)
t = total2
less2 = 0

for i in range(37):
    t -= EQ2[i]
    GT2[i] = t
    LT2[i] = less2
    less2 += EQ2[i]


print EQ
print LT
print GT
print

print EQ2
print LT2
print GT2
print




P = []
wins = 0
W = []

totes = 0

for p2 in range(37):
    W += [0]
    for p1 in range(p2,37):
        if p1 > p2:
            W[p2] += EQ[p1]*EQ2[p2]
            wins += EQ[p1]*EQ2[p2]
        totes += EQ[p1]*EQ2[p2]
        
print W
print wins 
print wins / 1.0 / total / total2

w = 0
totes2 = 0

for i in range(37):
    w += EQ[i]*LT2[i]
    totes2 += EQ[i]*total2
    
print w     
print totes
print total * total2, total + total2
print w/1.0/totes2
print totes2
print 4**4*6**6