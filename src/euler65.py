'''
Created on 2011-04-14

@author: Warren
'''
def approx(a,L):
    if len(L)>1:
        n,d = approx(L[0],L[1:])
        return a*n+d,n
    else:
        return a*L[0]+1,L[0]
    
L = []
for k in range(1,100):
    L += [1,2*k,1]

print L
for i in range(1,100):
    print i+1, approx(2,L[:i])
    
n,d = approx(2,L[:99])
sumdig = 0
for dig in list(str(n)):
    sumdig += int(dig)
print sumdig