'''
Created on Mar 27, 2013

@author: W
'''
def minsubarraykzeros(A,k):
    n = len(A)
    Z = [0]*(k+1)
    count = 0
    i=0
    mina = n
    while count < k:
        if A[i]==0:
            Z[count] = i
            count +=1
        i +=1
    mina = min(Z[k-1] - Z[0],mina)
    while i<n:
        if A[i]==0:
            Z += [i]
            Z = Z[1:]
            mina = min(Z[k-1] - Z[0],mina)
        i+=1
    return mina

print minsubarraykzeros([1,1,0,1,0,1,0,0,0,1,1], 4)
        