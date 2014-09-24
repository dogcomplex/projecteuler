'''
Created on 2010-11-25

@author: Warren
'''
import math
'''
Pents = [1]
i = 1
diff = 5
stop = False
# increases by 3n+1 each time
while(not stop):
    olddif = diff
    diff += 3*i+1
    n = 10
    while(not stop):
        d=0
        m=1
        while d <= diff:
            d = m*(3*m+6*n-1)/2
            if d==diff:
                print diff, n,m
                stop = True
                break
            m+=1
            print diff, d, m, n
        n +=1
    i +=1
'''
       
Pents = []
Bigs = {}
p = 1
i = 1
while True:
    Pents += [p]
    if p in Bigs:
        print p, Bigs[p], p-Bigs[p]
        break
    for p2 in Pents:
        if p-p2 in Pents:
            Bigs[p+p2]=p
        print p, p2
    p +=3*i +1
    i +=1
    
    
        
        
        
        
    