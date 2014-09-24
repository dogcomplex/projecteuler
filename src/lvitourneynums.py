'''
Created on Jul 18, 2011

@author: W
'''
lowercut = 20
uppercut = 50
for k in range(2,8):
    print k, 'rounds:'
    for i in range(k+1):
        s = 2**i * 3**(k-i) 
        if lowercut < s < uppercut:
            print s, i, 'rounds of 2,', k-i, 'rounds of 3'
    print