'''
Created on May 27, 2014

@author: W
'''
'''
Created on Apr 15, 2013

@author: W
'''
BOARD = [(25,'SBull'),(50,'DBull')]
DOUBLES = [(50,'DBull')]
for i in range(1,21):
    BOARD += [(i,'S'+str(i)),(2*i,'D'+str(i)),(3*i,'T'+str(i))]
    DOUBLES += [(2*i,'D'+str(i))]
    
S = set(DOUBLES)

for p,name in BOARD:
    for dp,dname in DOUBLES:
        S.add((p+dp, name + ' ' + dname ))

for p1,name1 in BOARD:
    for p2,name2 in BOARD:
        for dp,dname in DOUBLES:
            if name1 <= name2:    
                    S.add((p1+p2+dp, name1 + ' ' + name2  + ' ' + dname ))
            else:
                S.add((p1+p2+dp, name2 + ' ' + name1  + ' ' + dname ))
print len(S)

F = set(S)
for p,name in S:
    if p>=100:
        F.remove((p,name))
        
print len(F),F