'''
Created on 2011-01-06

@author: Warren
'''
import math

def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def sumsquare(P,n):
    i=1
    while i <= math.sqrt(int(n/2)):
        if isprime(n - 2*i**2):
            return i
        i +=1
    return False

P = []
for x in range(1,10000,2):
    y =sumsquare(P,x)
    if not y and not isprime(x):
        print x, y
    