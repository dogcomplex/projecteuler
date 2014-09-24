'''
Created on 2010-11-03

@author: Warren
'''
from decimal import *
'''
L = []

for d in range(2,10):
    L += [(d,0,0,0,0)]

round = 0
while len(L)>1:
    (d, start, pos, end, offset) = L.pop(0)
    frac = int(10**(round)/d)
    sfrac = str(frac)
    if len(sfrac)<round:
        continue
    if pos==0:
        for i in range(offset,round):
            if int(sfrac[i])==int(sfrac[round]):
                offset = i
                start = i
'''
max = [0,0,0]
PREC = 3000
CK = 1000
getcontext().prec = PREC
for d in range(2,1000):
    frac = Decimal(1)/Decimal(d)
    sfrac = (str(frac)[:-4])[::-1]
    if len(sfrac)!=PREC:
        #print d, "nocycle"
        continue
    chunk = sfrac[:CK]
    i = sfrac.find(chunk,1)
    if i>0:
        print d,i, frac
        if i>max[1]:
            max[0]=d
            max[1]=i
            max[2]=frac
print max
''' 
id = sfrac[-1]
for i,x in enumerate(reversed(sfrac[:-1])):
    if x==id:
        fail=False
        if i==0:
            fail==True
        for j in range(i):
            if sfrac[203-j]!=sfrac[202-i-j]:
                fail=True
        if not fail:
            print d, i, sfrac
            break
#print d, "nocycle"
'''