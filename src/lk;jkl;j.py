'''
Created on Apr 4, 2012

@author: W
'''
for i in range(1,10):
    for j in range(1,10):
        x = i*1./10
        y = j*1./10
        print  x,y, x*(1-y)*1./(y*(1-x) + x*(1-y))