'''
Created on May 6, 2014

@author: W
'''

#1389026625
#1058921220
from math import *

j = 0
a = 1058921220
while a < 1389026626:
    s = str(a*a)
    check = True
    print s
    j+=1
    for i in range(0,9):
        if int(s[2*i])<i+1:
            check = False
            print '<b4', i, a, s
            new = s[:2*i]+str(i+1)+'0'*len(s[2*i+1:])
            newa = int(sqrt(int(new)))
            if a==newa:
                a=newa+1
                new = a*a
            else:
                a=newa
            print '<af', i, a, new
            break
        if int(s[2*i])>i+1:
            check = False
            print '>b4', i,  a, s
            while s[2*i-1]=='9':
                i-=1
            new = s[:2*i-1] + str(int(s[2*i-1])+1) + str(i+1) +'0'*len(s[2*i+1:])
            newa = int(sqrt(int(new)))
            if a==newa:
                a=newa+1
                new = a*a
            else:
                a=newa
            print '>af', i,  a, new
            break
    if check:
        if s[-1]=='0':
            print 'dece',s, a
            break
        else:
            print 'soclose', s, a
            break
    