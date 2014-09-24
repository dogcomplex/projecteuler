'''
Created on Nov 2, 2011

@author: W
'''

import random


division = 0
sumX = 0
sumY = 0
n = 1000000

for i in range(n):
    x = random.random()
    y = random.random()
    if x> y:
        temp = x
        x = y
        y = temp
        
    division += (x*1./y)
    sumX += x
    sumY += y 
 
print division, sumX, sumY, '   OR  ', division/n, sumX/sumY, (division/n)/(sumX/sumY)