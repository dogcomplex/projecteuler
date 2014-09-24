'''
Created on Apr 21, 2013

@author: W

'''



import itertools 
from operator import itemgetter, attrgetter


def genprimes(n):
    Primes = [2,3]
    i = 5
    while i < n:
        isprime = True
        for p in Primes:
            if i%p==0:
                isprime = False
                break
        if isprime:
            Primes += [i]
        i+=2
    return Primes
        

def primefactors(n):
    A = []
    B=[]
    if n==1:
        return set([])
    for p in Primes:
        if p>n:
            break
        if n%p == 0:
            A += [p]
    return set(A)


FACTORS = []
N = 120000
Primes = genprimes(N)
print "gen'd primes"


for n in range(N):
    FACTORS += [primefactors(n)]
    if n%10000==0:
        print n

RAD = [0]
for n in range(1,N):
    x = 1
    for f in FACTORS[n]:
        x *= f
    RAD += [x]


zipRAD = zip(RAD,range(N))
print zipRAD[129],RAD[129]

zipRAD.sort()


hasRAD = {}
for n in range(N):
    if not hasRAD.has_key(RAD[n]):
        hasRAD[RAD[n]] = [n]
    else:
        hasRAD[RAD[n]] += [n]

for S in hasRAD.values():
    S.sort()

print FACTORS[504],RAD[504]



'''
count = 0
sumc = 0
C = []
for c in range(2,N):
    for a in range(1,c/2):
        b = c-a
        if RAD[a]*RAD[b]*RAD[c]<c:
            if FACTORS[a].isdisjoint(FACTORS[b]) and FACTORS[b].isdisjoint(FACTORS[c]) and FACTORS[a].isdisjoint(FACTORS[c]):
                print a,b,c
                count +=1
                sumc += c   
                C += [c]
print count,sumc

print C  
for i in C:
    print i, i/RAD[i], RAD[i], FACTORS[i]
    
print RAD
'''         


count = 0
sumc = 0
C = []
for c in range(2,N):
    for rada in hasRAD.keys():
        if rada > c/RAD[c]:
            break
        for a in hasRAD[rada]:
            if a >= c/2:
                break
            b=c-a
            if RAD[a]*RAD[b]*RAD[c]<c:
                if FACTORS[a].isdisjoint(FACTORS[b]) and FACTORS[b].isdisjoint(FACTORS[c]) and FACTORS[a].isdisjoint(FACTORS[c]):
                    print a,b,c
                    count +=1
                    sumc += c   
                    C += [c]

print count, sumc
print C
        
                    
'''        
    for radab in range(1,c/RAD[c]+1):
         if RAD[c]%radab==0:
             for a in range(1,c/2):
                  
'''