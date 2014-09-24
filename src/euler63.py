'''
Created on 2011-04-13

@author: Warren
'''
sum = 0
for b in range(2,100):
    a = 2
    L = []
    while True:
        x = a**b
        if x >= 10**b:
            break
        if x >= 10**(b-1):
            L +=[(a,b)]           
        a += 1
    print b,L
    sum += len(L)
print sum

