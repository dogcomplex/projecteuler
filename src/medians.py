'''
Created on 2011-02-06

@author: Warren
'''
from math import *
import random

def meds(A,B,n):
    if n==2:
        if A[0]>B[0]:
            return A[0]
        else:
            return B[0]
    #print n, A, B
 
    if A[n/2-1]<B[n/2-1]:
        return meds(A[int(ceil(n/2.)-1):],B[:n/2+1],n/2+1)
    else:
        return meds(A[:n/2+1],B[int(ceil(n/2.)-1):],n/2+1)


def meds2(A,B,astart,aend,bstart,bend,n):
    if n==2:
        if A[astart]>B[bstart]:
            return A[astart]
        else:
            return B[bstart]
    
    if n%2==0:
        if A[astart + n/2-1]<B[bstart + n/2-1]:
            return meds2(A,B,astart+n/2-1,aend,bstart,bend+n/2,n/2+1)
        else:
            return meds2(A,B,astart,aend+n/2,bstart+n/2-1,bend,n/2+1)
    else:
        if A[astart + n/2-1]<B[bstart + n/2-1]:
            return meds2(A,B,astart+n/2,aend,bstart,bend+n/2,n/2+1)
        else:
            return meds2(A,B,astart,aend+n/2,bstart+n/2,bend,n/2+1)
    
n = 8
A = [1, 3, 5, 9, 10, 11, 13, 15] 
B = list(range(2*n))
for a in A:
    B.remove(a)
meds(A,B,n)


for n in range(2,60):
    A = random.sample(list(range(2*n)),n)
    A.sort()
    B = list(range(2*n))
    for a in A:
        B.remove(a)
    C = A + B
    C.sort()
    print n, C[n-1], meds(A,B,n)
    
