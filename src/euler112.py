'''
Created on May 4, 2014

@author: W
'''
def bounceit(n):
    L =list(str(n))
    up = 0
    down = 0
    x = L[0]
    for c in L[1:]:
        if c > x:
            up = 1
            if down:
                return True
        if c < x:
            down = 1
            if up:
                return True
        x = c 
    if up and down:
        return True
    return False


c = 0
i = 0
for n in range(1,2178100):
    if bounceit(n):
        c +=1
    i +=1
   
    if c/1.0/i == .99:
        print i,c,n, c/1.0/i
        break
    
