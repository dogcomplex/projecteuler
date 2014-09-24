'''
Created on 11-Nov-09

@author: Warren
'''
C = {1:1}
D = {1:[1]}
Divs = {}

def properDivs(n):
    sum = 1
    for p in range(2,int(n**.5)+1):
        #print p, sum
        if n%p==0:
            sum += p
            q = int(n/p)
            if q != p and q !=1:
                sum +=q
                #print(n,p,q)
    return sum 


def cycleCount(n):
    global C
    L = [n]
    count = 1
    next = n
    while True:
        next = properDivs(next)
        #print (n,len(L))
        if next >= 1000000:
            for x in L:
                C[x] =-1
            return -1, L
        if next in L:
            pos = L.index(next)
            cycleLen = len(L)-pos
            for y in L[pos:]:
                C[y] =cycleLen
            for i,y in enumerate(L[:pos]):
                C[y] =count-i
            return len(L),L
        if C.get(next,False) != False:
            if C[next] < 0:
                count = -1
            else:
                count += C[next]
            for i,y in enumerate(L):
                C[y] =count-i
            return count, L
        count +=1
        L.append(next)

def cycleCount2(n):
    global D
    L = [n]
    next = n
    while True:
        next = properDivs(next)
        if next >= 1000000:
            for x in L:
                D[x] = [1000000]
            return -1, L+[next]
        if next in L:
            pos = L.index(next)
            for i,x in enumerate(L[pos:]):
                D[x] =L[pos+i:] + L[pos:pos+i]
            for i,x in enumerate(L[:pos]):
                D[x] =L[i:]
            return len(L),L
        if D.get(next,False) != False:
            if 1000000 in D[next]:
                for y in L:
                    D[y] = [1000000]
                return -1, L+D[next]
            else:
                for i,y in enumerate(D[next]):
                    if y in L:
                        pos = L.index(y)
                        for j,x in enumerate(L[:pos]):
                            D[x] = L[j:] + D[next][:i]
                        for j,x in enumerate(L[pos:]):
                            D[x] = L[pos+j:] + D[next][:i] + L[pos:pos+j]
                        return len(L + D[next][:i]),L + D[next][:i]
        L.append(next)


def cycleCount3(n):
    global D
    L = [n]
    next = n
    while True:
        next = properDivs(next)
        if next >= 1000000:
            for x in L:
                D[x] = [1000000]
            return -1, L+[next]
        if next in L:
            pos = L.index(next)
            for x in L:
                D[x] =L[pos:]
            return len(L[pos:]),L[pos:]
        if D.get(next,False) != False:
            if 1000000 in D[next]:
                for y in L:
                    D[y] = [1000000]
                return -1, L+D[next]
            else:
                for x in L:
                    D[x] = D[next]
                return len(D[next]),D[next]
        L.append(next)



max = 0

print(cycleCount3(12496))
print(D[14264])
print(cycleCount3(15472))
print(properDivs(17716))

R = []

bigX = [100000000]
for start in range(1,1000000):
    count, X = cycleCount3(start)
    if start%10000==0: 
        print(start, max, count, X)
    if count >= max:
        max = count
        bigX = X
print(max,min(bigX),len(set(bigX)),bigX)
#print(D)


    

