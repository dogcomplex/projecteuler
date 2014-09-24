'''
Created on May 2, 2014

@author: W
'''

count = 0
L = {}
N = 1000001
for n in xrange(100000000,1000000001):
    rev = int(str(n)[::-1])
    r = n + rev

    invalid = False
    if str(n)[0]=='0' or str(n)[-1]=='0':
        invalid = True
    for c in str(r):
        if int(c)%2==0:
            invalid = True
    if not invalid:
        print n, rev, r
        count +=1
        if L.has_key(r):
            L[r] += [(n,rev)]
        else:
            L[r] = [(n,rev)]
        
print count
#print L
K = L.keys()
K.sort()
for i in K:
    print len(L[i]),
print
print count