'''
Created on May 7, 2014

@author: W
'''
from math import sqrt

count = 0
T = 10000000
for x in xrange(1,T,2):
	y = x+1
	a = (x*x - y*y/4.0)**.5*(y*y/4.0)
	if a == int(a) and x+x+y <= T:
		count += x+x+y
		
	y = x-1
	a = (x*x - y*y/4.0)**.5*(y*y/4.0)
	if a == int(a) and x+x+y <= T:
		count += x+x+y
		
	if x+x+y >T:
		break
print count

	
