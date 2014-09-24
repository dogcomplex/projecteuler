'''
Created on Apr 15, 2013

@author: W
'''

import math

def g(i): #of digits (for any d) less than 10**i
    if i==1:
        return 1
    else:
        return 10**(i-1) + 10*G[i-2]

def gnd(n,d): # of digits==d less than n
    i = len(str(n))-1
    j=i
    x = 0
    while j>=0:
        digit = int(str(n)[i-j])
        if j==0:
            if digit>d:
                x +=1
        else:
            if digit>d:
                x += 10**j
                #print 'a',digit,j,x
            if digit==d:
                if str(n)[i-j+1:]!='':
                    x += int(str(n)[i-j+1:])
                    #print 'b',str(n)[i-j+1:],x
            #print 'c', x,i,j
            x += digit*G[j-1]
            #print 'd',digit,G[j-1],x
        j-=1
    return x
          
    
    
G = [1]
for i in range(2,100):
    G += [g(i)] 
print G

def sumg(i,d): #sum solutions for d to f(n,d)=n for n < 10**i
    if i==1:
        return 2
    else:
        return 

def f(n,d):
    sum =0
    S = str(n)
    for c in S:
        if int(c) == d:
            sum +=1
    return sum

'''
S = [0]*10   
Snn = [0]*10
N =4101
for d in range(1,10):
    for i in range(N):
        S[d] += f(i,1)
        if i==S[d]:
            Snn[d] += i
        print i,d, S[d],Snn[d]
print S
print Snn
'''

N = 4101
d=2
print gnd(N,d)

'''
for i in range(2,len(G)):
    if 10**i*(d+1) < gnd(10**i*(d+1),d):
        break
print i,10**i*(d+1), gnd(10**i*(d+1),d)

'''
'''
for i in range(1,30):
    for j in [-1,0,1]:
        
        for d=2:
        12000
        13000
        ...
        13333
        20000
        22000
        23000
        30000
        32000
        33000
        
        n = (d+j)*int('1'*i)+1
        print n, gnd(n,d), n-gnd(n,d)
'''

localsum = 0
totalsum = 0
max = 0
for n in range(10000000):
    count =0
    N = n
    while n>0:
        c = n%10
        if c==d:
            count +=1
        n /=10
    
    localsum+=count
    totalsum+=count
    if count > max:
        #print N, count, max, localsum,totalsum,n-totalsum
        max = count
        localsum = 0
    if (n-totalsum <0 and n-1-(totalsum-count) >=0) or (n-totalsum >0 and n-1-(totalsum-count) <=0):
        print N, count, max, localsum,totalsum,n-totalsum
            


