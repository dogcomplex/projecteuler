'''
Created on 2011-02-07

@author: Warren
'''
sum = 0
count = 0

def next(B,n,k):
    global sum,count
    j = n
    while B[j]==0:
        j -=1
    p = n-j
    while B[j]==1:
        j -=1
    q = n-j-p
    sum += n-j +1
    count +=1
    if j==0:
        return 0
    print B, p, q, p+q+1, n-j+1
    B[j]=1
    for i in range (1,p+2):
        B[i+j] = 0
    for i in reversed(range(1,q)):
        B[n-i+1] = 1
    return 1

n = 13
k=8
B = [-1]
for i in range(n-k):
    B.append(0)
for i in range(k):
    B.append(1)
        
sum=0
count=0
while next(B,n,k):
    i +=1
print sum
print (n+2)*(n+1)/(k+1)/(n-k-1)*count
print 2*n/k * count
print n*count