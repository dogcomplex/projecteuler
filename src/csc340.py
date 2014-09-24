'''
Created on 2011-01-21

@author: Warren
'''
def binomseries(x,n, epsilon):
    s = float(1)
    ds= float(1)
    i=1
    while abs(ds) > epsilon:
        ds *= n-(i-1)
        ds *= x
        ds /= i
        s += ds
        i +=1
        print '%.15f' % s  

#binomseries(.0001,.5, 10**-16)

def J(n,x):
    if n==0 and x==1:
        return 0.7651976865
    if n==1 and x==1:
        return 0.4400505857
    y = 2*(n-1)/x * J(n-1,x) - J(n-2,x)
    return y

'''for i in range(1,21):
    print i, '%.25f' % (J(i,1)/J(i-1,1))'''
    
def noZeroInts(epsilon):
    ds = float(1)
    i=1
    s = float(0)
    mark = 1
    while ds > epsilon:
        if '0' not in str(i): 
            ds = float(1)/i 
            s +=ds
        print i,'%.25f' % s, '%.25f' % ds
        i +=1        

#noZeroInts(10**-15)

''' Sums all reciprocals not containing 0 starting with n followed by k digits'''
def noZeros(n,k):
    if n>0:
        sum = 1.0/n
    else:
        '''special case for first call'''
        sum = 0
    ''' sum of NoZeros(nx,k-1) - where x is 1-9 '''
    for i in range(n*10+1,n*10+10):
        if k==1:
            sum += 10.0/i
        else:
            sum += noZeros(i,k-1)
    return sum
        

for i in range(1,8):
    print i,noZeros(0,i)  
    
    

        
