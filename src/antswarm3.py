
from random import random




def antswarm():
    n = 100
    m = 2
    k = .05
    quorum = .8
    C = 1
        
    Y[i] = [0]*m
    dY[i] = [0]*m    
        
    def Q(i):
        q = [.5,.4]
        return q[i] 
        
    dt = 1
    home = n
    for i in range(m):
        
        
        steals = 0
        for j in range(m):
            if i!=j:
                steals += f(Y[i])
        
        wanders = home*Q(i)
        
        dY[i] = (-k*Y[i] -w*steals + wanders)*dt + c*d
            
antswarm()