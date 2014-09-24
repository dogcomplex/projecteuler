'''
Created on Apr 22, 2013

@author: W
'''

A = []

N = 10000
D = 20
count =1
for n in range(1,N):
    for i in range(1,D):
        x = n**i
        sum = 0
        j =0
        while x>0:
            sum += x%10
            x /=10
            j +=1
        if sum==n and j>1:
            A +=[(n**i,n,i)]
            print count, sum, n,i,n**i
            count +=1

A.sort()
print A
print A[29]