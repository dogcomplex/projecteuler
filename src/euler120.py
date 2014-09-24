'''
Created on Apr 27, 2014

@author: W
'''
import math

s = 0
for a in range(3,1001):
    n=0
    maxr = 0
    while True:
        if 2*n >= a:
            n+=1
            break
        r = n*2*a
        n+=1
        if r > maxr:
            maxr = r
            #print a, n, r
    print a, maxr
    s += maxr
print s