'''
Created on Oct 4, 2012

@author: W
'''
def stri(X):
    s = ""
    for i in range(10):
        if i in X:
            s += str(i)
    return s

import copy

def add(x,X):
    for i in range(len(X)):
        if X[i] > str(x):
            return X[:i] + str(x) + X[i:]
    return X + str(x)
        

def alph(X,Y):
    if X<Y:
        return (X,Y)
    else:
        return (Y,X)

def sixify(S):
    S44 = []
    for X,Y in S:
        if X==Y:
            print 'err'
        if str(6) in X:
            Xnew = X.replace('6', '')
            Xnew = add(9,Xnew)
            S44 += [alph(Xnew,Y)]
            if str(6) in Y:
                Ynew = Y.replace('6', '')
                Ynew = add(9,Ynew)
                S44 += [alph(Xnew,Ynew)]
        if str(6) in Y:
            Ynew = Y.replace('6', '')
            Ynew = add(9,Ynew)
            S44 += [alph(X,Ynew)]
    S44 = set(S44)
    return S44.union(S)

L = [[[0],[1]]]
for (x,y) in [(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(8,1)]:
    L2 = []
    for [X,Y] in L:
        X2 = copy.copy(X)
        Y2 = copy.copy(Y)
        X += [x]
        Y += [y]
        X2 += [y]
        Y2 += [x]
        
        L2 += [[X2,Y2]]
    L += L2


S6 = []
S5 = []
S4 = []
S3 = []
for [X,Y] in L:
    S1 = stri(X)
    S2 = stri(Y)
    if len(S1)<=6 and len(S2)<=6:
        if len(S1)==6 and len(S2)==6:
            S6 += [alph(S1,S2)]
        elif len(S1)>=5 and len(S2)>=5:
            S5 += [alph(S1,S2)]
        elif len(S1)>=4 and len(S2)>=4:
            S4 += [alph(S1,S2)]
        else:
            S3 += [alph(S1,S2)]
    

print len(S6),S6
print len(S5),S5
print len(S4),S4
print S3
print

S6 = set(S6)
S5 = set(S5)
S4 = set(S4)

print len(S6), S6
print len(S5), S5
print len(S4), S4
print

S4 = sixify(S4)
S5 = sixify(S5)
S6 = sixify(S6)


print len(S6), S6
print len(S5), S5
print len(S4), S4
print


S6 = set(S6)
print len(S6), S6
S5 = set(S5)
print len(S5), S5
S4 = set(S4)
print len(S4), S4
print


S55 = []
for (X,Y) in S4:
    if len(X)==4:
        if len(Y)==4:
            print "ballllss"
        for i in range(10):
            if str(i) not in X:
                newX = add(i,X)
                S55 += [alph(newX,Y)]
    if len(Y)==4:
        for i in range(10):
            if str(i) not in Y:
                newY = add(i,Y)
                S55 += [alph(X,newY)]  

S55 = set(S55)
S5.union(S55)


print len(S6),S6
print len(S5),S5
print


S56 = []
for (X,Y) in S5:
    #if len(X.difference(Y))<=1 or len(Y.difference(X))<=1:
    #    print X,Y 
    if len(X)<6:
        for i in range(10):
            if str(i) not in X:
                newX = add(i,X)
                S56 += [alph(newX,Y)]
    if len(Y)<6:
        for i in range(10):
            if str(i) not in Y:
                newY = add(i,Y)
                S56 += [alph(X,newY)]        

S56 = set(S56)
print len(S6),S6
print len(S56),S56
print

S66 = []
for (X,Y) in S56:
    #if len(X.difference(Y))<=1 or len(Y.difference(X))<=1:
    #    print X,Y 
    if len(X)<6:
        if len(Y)<6:
            print X,Y
        for i in range(10):
            if str(i) not in X:
                newX = add(i,X)
                S66 += [alph(newX,Y)]

    if len(Y)<6:
        if len(X)<6:
            print X,Y
        for i in range(10):
            if str(i) not in Y:
                newY = add(i,Y)
                S66 += [alph(X,newY)]        

S66 = set(S66)

print len(S6),S6
print len(S66),S66
print



S = S6.union(S66)

print len(S),S
S = list(S)
S.sort()
print S

def sanitycheck(X,Y):
    if len(X)>6 or len(Y)>6:
        return False
    X = X.replace('9','6')
    Y = Y.replace('9','6')
    for (x,y) in [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(6,4),(8,1)]:
        x = str(x)
        y = str(y)
        if not( (x in X and y in Y) or (y in X and x in Y)):
            return False
    return True

#sanity
for X,Y in S:
    if not sanitycheck(X,Y):
        print X,Y
S2 = []
for X,Y in S:
    S2 += [alph(X,Y)]
S2 = set(S2)
print len(S2), S2       
for X,Y in S:
    if X==Y:
        print "inconceivable"
    

'''bruteforce'''
T = []
for i in range(10):
    for j in range(10):
        if i==j:
            continue
        for l in range(10):
            if l==i or l==j:
                continue
            for k in range(10):
                if j==i or j==l or j==k:
                    continue
                s = ''
                for ii in range(10):
                    if ii not in [i,j,k,l]:
                        s += str(ii)
                T += [s]
T = set(T)
print len(T), T

R = []
for X in T:
    for Y in T:
        if sanitycheck(X,Y):
            R += [alph(X,Y)]

print len(R)
R = set(R)
print len(R)
