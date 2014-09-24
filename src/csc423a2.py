'''
Created on Feb 21, 2012

@author: W
'''
from random import random

def find():
    N = 2
    while True:
        Y = int((N**2/2)**.5 - 1)
        Y2 = int(((N+1)**2/2)**.5 +2)
        #print N, len(range(Y,Y2+1)), Y,Y2, Y*(Y-1)*1./(N*(N-1)), Y2*(Y2-1)*1./(N*(N-1))
        for y in range(Y,Y2+1):
            if 2*y*(y-1)==N*(N-1):
                print y,N, y*1./N
                break
        N +=1

find()