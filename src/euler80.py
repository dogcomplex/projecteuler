'''
Created on May 5, 2014

@author: W
'''

from math import *
from decimal import *
getcontext().prec = 105

SUM = 0
for n in range(1,101):
    if sqrt(n)!=int(sqrt(n)):
        s =  str(Decimal(n).sqrt())
        sum = 0
        for c in s[:101]:
            if c !='.':
                sum += int(c)
        if n==2:
            print sum, s[2:][:100]
        SUM += sum
print SUM

x = Decimal(2)
a = Decimal(2)
for i in range(100):
    x = (x+a/x)/Decimal(2.0)
    print x, a