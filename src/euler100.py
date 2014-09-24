'''
Created on Apr 28, 2014

@author: W
'''

'''
i = 10
Squaredifs = {}
while True:
    t2 = i*i-i
    if t2%2==0:
        if Squaredifs.has_key(t2/2):
            print Squaredifs[t2/2], t2, i
            print Squaredifs[t2/2]**2-Squaredifs[t2/2], t2, (Squaredifs[t2/2]**2-Squaredifs[t2/2]) / 1.0/ t2
            break
        Squaredifs[t2]=i
    i=2*i-1
    print i, t2, (i*2-i) / 1.0 / t2
    
'''
b0=1
b = 3

t0 =1 
t = 4
while True:
    b2 = 6*b-b0-2
    b0 = b
    b = b2

    t2 = 6*t-t0-2
    t0 = t 
    t = t2 

    if t>1000000000000:
        print b, t, (b*b-b)/1.0/(t*t-t)
        break
    