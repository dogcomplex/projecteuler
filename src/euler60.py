'''
Created on May 5, 2014

@author: W
'''

import math
import collections 

def isprime(p):
    if P.has_key(p):
        return True
    if p<=1:
        return False
    if p%2==0 and p!=2:
        return False
    for i in range(2,int(math.sqrt(p))+1):
        if p%i==0:
            return False

    return True
 
def isprime2(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    if not num%2 or not num%3:
        return False
    for i in range(5, int(num**0.5) + 1, 6):   
        if not num%i or not num%(i + 2):
            return False
    return True
 
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
 
'''
P = {}
PS = []

for p in range(10000):
    if isprime(p):
        for i, S in enumerate(PS):
            allclear = True
            for pp in S:
                if not isprime(int(str(p)+str(pp))) or not isprime(int(str(pp)+str(p))):
                    allclear=False
                    break
            if allclear:
                PS[i] += [p]
                if len(S)>=4:
                    print S, p

        PS += [[p]]
'''

Counts = {}
P =  {}
Pairs = {}
for n in range(3,1000,2):
    if is_prime(n):
        P[n]=n
        none = True
        for p in P.keys():
            if p>=n:
                break
            '''
            pup = 10**len(str(p))
            nup = 10**len(str(p))
            if (n*pup)%p==0 or (p*nup)%n==0:
                continue
            '''
            if is_prime(int(str(p)+str(n))) and is_prime(int(str(n)+str(p))):
                none = False
                if p in Counts:
                    Counts[p] +=1
                else:
                    Counts[p] = 1
                if Pairs.has_key(p):
                    Pairs[p] += [n]
                else:
                    Pairs[p] = [n]
                if Pairs.has_key(n):
                    Pairs[n] += [p]
                else:
                    Pairs[n] = [p]
                #if n==673:
                #    print n,p,isprime(int(str(109)+str(n))) and isprime(int(str(n)+str(109)))
        
        


def intersect3(L,L2):
    return len(set(L).intersection(set(L2))) >= 3
            


print Pairs[109], P[673]
for i in range(10):
    for p in Pairs.keys():
        if len(Pairs[p])<4:
            del Pairs[p]
            continue
    
    for p in Pairs.keys():
        
        if not Pairs.has_key(p):
            continue
        
        for pp in Pairs[p]:
            if Pairs.has_key(pp) and len(Pairs[pp])<4:
                del Pairs[pp]
                Pairs[p].remove(pp)
                continue
            if not Pairs.has_key(pp):
                Pairs[p].remove(pp)
                continue 
            
            if not intersect3(Pairs[p],Pairs[pp]):
                Pairs[p].remove(pp)
                Pairs[pp].remove(p)
        
        if len(Pairs[p])<4:
            del Pairs[p]
            continue
    
for k in sorted(Counts.keys()):
    print k, Counts[k]
        
'''
META
stuck.
Seems like we might need some smarter way of generating the original pair lists. The pruning after is negligible. 
It's just the initial graph construction that's the problem.  Maybe there's a secret in the concatenation that eliminates primes early on so we never have to recheck them?
Could only test those with cliques above a certain threshold, but might eliminate early possibilities.

better prime test? 

approx tests initially, then double check on prune? yes.
Nope...
still too slow even with miller-rabin style test

even removing all prime testing and just letting it do everything is too much
gotta prune somehow.

'''