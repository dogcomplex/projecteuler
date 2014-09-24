'''
Created on May 8, 2014

@author: W
'''




import math

def gen_primes():
    D = {}
    q = 2  # first integer to test for primality.
    
    while True:
        if q not in D:
            # not marked composite, must be prime  
            yield q 
            
            #first multiple of q not already marked
            D[q * q] = [q] 
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            # no longer need D[q], free memory
            del D[q]
            
        q += 1

primes = gen_primes()
c = 0
P = []
for p in primes:
    c +=1
    if p >10**8:
        break
    P += [(p,c)]
    print p, c
    
'''
def isprime(n):
    if n<=1:
        return False
    if n%2==0 and n!=2:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True


P = []

def isprimeish(n,P):
    if n <=1:
        return False
    if n==2:
        P += [n]
        return False
    prime = True
    for p in P:
        if n%p==0:
            prime = False
            q = n/p
            if q in P: # could be slow
                return True
    if prime:
        P += [n]
    return False
        


for n in xrange(10**8/2):
    if isprime(n):
        P +=[(n,len(P))]
    if n%10000==0:
        print n
'''
            