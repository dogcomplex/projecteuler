'''
Created on 2009-10-06

@author: Warren
'''
import math
import gmpy

n = 5
k = 2
B = []*n



def Combin(j,m):
    print(B, j, m)
    global B, n, k
    if j > n:
        print("A:",B)
    else:
        if k-m < n-j+1:
            B[j-1] = 0
            Combin(j+1, m)
        if m<k:
            B[j-1] = 1
            Combin(j+1,m+1)
            
def Colex(n,k):
    print(B,n,k)
    if k==0:
        print(B)
    else:
        if k<n:
            B[n] = 0
            Colex(n-1,k)
        B[n]=1
        Colex(n-1,k-1)
        B[n]=0
           
def Colex2(n,k,pos):
    global B,N
    if k==0:
        print(gmpy.digits(B,2).zfill(N)) 
    else:
        if k<n:
            B &= pos
            Colex2(n-1,k, pos>>1)
        B |= pos
        Colex2(n-1,k-1,pos>>1)
        B &= pos
           
#Colex(n,k)

N = n
k = 2
B = [0]*(n+1)
B = 0

pos = 1<<n
Colex2(n,k,pos)