'''
Created on May 27, 2014

@author: W
'''

F = {}
F[0]=1
F[1]=1

    
def f(M,n):
    if n in F:
        return F[n]
    total = 0
    if n>0:
        total += f(M,n-1)  #black tile
    if n==0:
        return 1
    elif n<0:
        return 0
    for m in range(M,n+1):
        if n-m-1>=0:
            total += f(M,n-m-1)
        elif n-m>=0:
            total += f(M,n-m)
        else:
            break
    F[n]=total
    return total


for n in range(0,10000):
    ff = f(50,n)
    print n,ff
    if ff >1000000:
        break
    