'''
Created on 2011-01-12

@author: Warren
'''
import math

def mindrop(n,j):
    if j==1:
        return n-1
    if j==2:
        return math.floor(math.sqrt(n))-1 + mindrop(math.ceil(math.sqrt(n)),j-1)
    
    min = n
    for interval in range(2,n):
        x = (interval-1) + mindrop(math.ceil(n*1.0/interval),j-1)
        if x < min:
            min = x

    print n,interval, min
    return min

def mindrop2(n,j):
    print n, j
    if j==1:
        return n-1
    return math.ceil(math.sqrt(n))-1 + mindrop(math.ceil(math.sqrt(n)),j-1)

def mindrop3(n,j,c):
    print n,j,c
    if n==1:
        return c
    if j==1:
        return c + n-1
    cut = min(math.ceil(math.pow(n, (j-1.0)/j)), math.ceil(n/2.0))
    return mindrop3(cut,j-1,c + math.ceil(n/cut)-1)
        
        
def mindrop4(L,j,c):
    n = len(L)
    if n==0:
        return c
    
    if n==2:
        c+=1
        if L[0]:
            return c
        else:
            return c
    if j==1:
        c+=1
        if L[0]:
            return c
        else:
            return mindrop4(L[1:],j,c)
    cut = int(min(math.ceil(math.pow(n, (j-1.0)/j)), math.ceil(n/2.0)))
    #print n,j,c, cut
    if cut==2 or True in L[:cut]:
        return mindrop4(L[:cut+1],j-1,c+1)
    else:
        return mindrop4(L[cut+1:],j,c+1)


print mindrop4([False]*100000,6,0),mindrop4([False]*100000,5,0)