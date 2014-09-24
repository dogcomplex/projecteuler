'''
Created on 2009-11-23

@author: Warren Koch, V00482478
'''

def Next():
    global p,q,L,par
    while L[p-1]==1:
        p -=1
    if p==1:
        return False
    if L[p-1]==2 and L[p-2]==1:
        L[p-1] =1
        par[p-1] = par[p-2]
    else:
        q = p-par[p-1]
        for i in range(p,n+1):
            L[i-1] = L[i-q-1]
            if q + par[i-q-1] < p:
                par[i-1] = par[i-q-1]
            else:
                par[i-1] = q+par[i-q-1]
        p = n
    return True

'''
for n in range(3,30):
    L = [i for i in range(n)]
    par = [i for i in range(n)]
    p = n
    q = p-par[p-1]
    
    i = 0
    sump = 0
    sumq = 0
    #print(i,p,q,L)
    while Next():
        sump += p
        sumq += q
        i+=1
        print(i,p,q,L)
    print(n, (n*i - sump*1.0)/i, (n*i - sumq*1.0)/i)
 '''  

'''
Observe, n-p stays constant (and actually shrinks) as n grows, while n-q grows with n.

3 0.0 2.0
4 0.333333333333 2.33333333333
5 0.25 3.0
6 0.210526315789 3.47368421053
7 0.170212765957 3.97872340426
8 0.149122807018 4.49122807018
9 0.129824561404 5.02807017544
10 0.118384401114 5.58913649025
11 0.108636610538 6.16838674633
12 0.101993704092 6.76096537251
13 0.0965158189828 7.36491790148
14 0.0924117432973 7.9774657285
15 0.0889761986106 8.59593440383
16 0.0862392726655 9.21996771179
17 0.0839132640042 9.84798990621
18 0.0819698133466 10.4796172112
19 0.0802921934235 11.1141883368
20 0.0788471153676 11.7514371919

This is because p==n for most of the computation, while q is almost always < n.
'''

def A(n,k):
     #print(n,k)  
     if k<0 or n<0:
         return []
     if k==0:
         return ["0"*n]
     if k==1:
         return ["0"*i+"1"+"0"*(n-i-1) for i in range(n)]
     if n==k:
         return ["1"*n]
     X =[i+"0" for i in A(n-1,k)]
     Y = [i+"11" for i in A(n-2,k-2)]
     Z = [i+"01" for i in reversed(A(n-2,k-1))]
     return X+Y+Z

def E(n,k):
     #print(n,k)  
     if k<0 or n<0:
         return []
     if k==0:
         return ["0"*n]
     if k==1:
         return ["0"*i+"1"+"0"*(n-i-1) for i in range(n)]
     if n==k:
         return ["1"*n]
     X =[i+"0" for i in E(n-1,k)]
     Y = [i+"01" for i in reversed(E(n-2,k-1))]
     Z = [i+"11" for i in E(n-2,k-2)]
     return X+Y+Z

def C(n,k):
     #print(n,k)  
     if k<0 or n<0:
         return []
     if k==0:
         return ["0"*n]
     if n==k:
         return ["1"*n]
     X =[i+"0" for i in C(n-1,k)]
     Y = [i+"01" for i in reversed(C(n-1,k-1))]
     return X+Y

def R(n,k,p):
     #print(n,k)  
     if k<0 or n<0 or k==n:
         return []
     if k==0:
         return ["0"*n]
     if n-1==k and p==1:
         return ["1"*(n-1)+"0"] + [i+"1" for i in R(n-1,k-1,1)]
     if p==1:
         X = [i+"0" for i in reversed(R(n-1,k,1))]
         Y = [i+"1" for i in R(n-1,k-1,2)]
     elif p==2:
         X = [i+"0" for i in R(n-1,k,1)]
         Y = [i+"1" for i in R(n-1,k-1,1)]
     return X+Y


  
c = 0
for i in A(6,3):
    c+=1
    x = len([c for c in i if c=='1'])
    print(i)



'''
A(n,k) outputs combinations in [Trans] order.  Observe:

111000
101100
011100
110100
100110
010110
001110
101010
011010
110010
100011
010011
001011
000111
100101
010101
001101
101001
011001
110001


is identical to [Trans] on page 133 of the text

'''