'''
Created on 2011-04-14

@author: Warren
'''
'''
from math import *

D = {}
limit = 1000
for d in range(2,limit):
    x = 2
    if sqrt(d) != int(sqrt(d)):
        while True:
            y = sqrt((x+1)*(x-1)*1./d)
            if int(y)==y:
                D[d]=x
                break
            print d,x,y
            x +=1   
print D
print max(D)
        
''' 
         
        

D = {}
limit = 1000
x = 2
missing = limit
found = True
while missing > 2:
    for y in range(1,x):
        if (x-1)*(x+1) % y**2==0:
            d =(x-1)*(x+1) / y**2
            if not D.has_key(d):
                if d <=limit:
                    missing -=1
                    print missing, (d,x,y)
                D[d] = x
    x +=1
            
            
    #print
print
print "Sols"
mx = 0
for d in D:
    if d <=limit:
        print d, D[d]
        mx = max(mx,D[d])
print mx
