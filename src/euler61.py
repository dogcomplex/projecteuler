'''
Created on 2011-01-09

@author: Warren
'''
import math
import itertools

L = []
for i in range(6):
    L.append([])
    
n=1
while True:
    x = n*(n+1)/2
    n+=1
    if x>=1000:
        break
while True:
    x = n*(n+1)/2
    n+=1
    if x>9999:
        break
    L[0].append(x)

n=1
while True:
    x = n**2
    n+=1
    if x>=1000:
        break
while True:
    x = n**2
    n+=1
    if x>9999:
        break
    L[1].append(x)

n=1
while True:
    x = n*(3*n-1)/2
    n+=1
    if x>=1000:
        break
while True:
    x = n*(3*n-1)/2
    n+=1
    if x>9999:
        break
    L[2].append(x)

n=1
while True:
    x = n*(2*n-1)
    n+=1
    if x>=1000:
        break
while True:
    x = n*(2*n-1)
    n+=1
    if x>9999:
        break
    L[3].append(x)
    
n=1
while True:
    x = n*(5*n-3)/2
    n+=1
    if x>=1000:
        break
while True:
    x = n*(5*n-3)/2
    n+=1
    if x>9999:
        break
    L[4].append(x)
    

n=1
while True:
    x = n*(3*n-2)
    n+=1
    if x>=1000:
        break
while True:
    x = n*(3*n-2)
    n+=1
    if x>9999:
        break
    L[5].append(x)
    
    
    
def limitset(n,L):
    S = []
    n = (n%100)*100
    if n<100:
        return []
    for x in L:
        if int((x/100))*100==n:
            S +=[x]
    return S

def recurse(x,L,d,Orig,I):

    if d>=5:
        if Orig in limitset(x,L[I[d]]):
            return [x]
        
        if Orig == x:
            print Orig, x, d
            return [x]
        else:
            return []
    X = [x]
    for y in limitset(x,L[I[d]]):
        Y = recurse(y,L,d+1,Orig,I)
        if len(Y)>=len(X):
            X = [x] + Y
    return X
        
X = [0,1,2,3,4,5]

stop = False
for I in itertools.permutations(X):
    for x in L[I[-1]]:
        X = recurse(x,L,0,x,I)
        #print I,X
        if len(X)>=6:
            print I,i,x,X
            s = 0
            for z in X:
                s +=z
            print s
            #stop = True
            #break
    if stop:
        break

        
            
        
