'''
Created on 2010-11-01

@author: Warren
'''
import heapq

H = []

N = 0
f = open(r'network.txt')
r=0
T = []
spent = 0
total = 0

for line in f:
    c=0
    T += [r]
    L = line[:-1].split(',')
    N = len(L)
    for v in L:
        if v !='-':
            total += int(v)
            H += [(int(v),c,r)]
        c+=1
    r+=1

total /=2

heapq.heapify(H)
count = N
while count>1:
    e = heapq.heappop(H)
    if T[e[1]]!=T[e[2]]:
        if T[e[1]]<T[e[2]]:
            new = T[e[1]]
            old = T[e[2]]
        else:
            new = T[e[2]]
            old = T[e[1]]
        for i,x in enumerate(T):
            if x==old:
                T[i]=new
        count -=1
        spent += e[0]
        #print spent, T
        print e, spent, total-spent, T
    print e
    
    
    