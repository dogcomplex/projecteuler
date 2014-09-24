'''
Created on Feb 10, 2011

@author: Warren
'''
import math

def coef(X,Y):
    n = len(X)
    A = []
    for y in Y:
        A.append(y*1.)
    for j in range(1,n):
        for i in reversed(range(j,n)):
            A[i] = (A[i]-A[i-1])/(X[i]-X[i-j])
        print 'iteration', j, A[j:]
    return A

def eval(A,X,t):
    n = len(X)
    s = A[n-1]
    for i in reversed(range(n-1)):
        #print 'interation', n-i-1, s
        s = s*(t-X[i])+A[i]
    return s


print '1 *****  p 124 question 1 '
X = [0,5,10,15]
Y = [1.792,1.519,1.308,1.140]
print 'COEF:'
A = coef(X,Y)
print 'A: ', A
print 'EVAL:'
print '%.16f' % eval(A,X,8.0)
print
print

print '2 ***** Equally spaced'
X = []
for i in range(9):
    X += [i/8.]
Y = []
for x in X:
    Y += [math.e**x]
print 'X:',X
print 'F(x)', Y
print 'COEF:'
A = coef(X,Y)
print 'A: ', A
print 'EVAL:'
print 't    e^t    p(t)    e^t-p(t)'
maxerror = -1
maxtheor = -1
for i in range(101):
    t = i/100.
    p = eval(A,X,t)
    maxerror = max(maxerror,abs(math.e**t - p))
    error = 1/362880. #1/9!
    error *= math.e**(t)
    for x in X:
        error *= abs(t-x)
    maxtheor = max(maxtheor,error)
    print '%.2f' % t, '%.16f' % math.e**t, '%.16f' % p, '%.16f' % abs(math.e**t - p), error
print 'max absolute error, e^t-p(t):', maxerror
print 'error bound for f(x) with equally spaced interpolation:', maxtheor

print
print '2 ***** BONUS Chebychev'
X = []
n = 9
for i in range(1,10):
    X += [1/2. + 1/2.*math.cos((2.*i-1)/(2.*9)*math.pi)]
X.sort()
Y = []
for x in X:
    Y += [math.e**x]
print 'X:',X
print 'F(x)', Y
print 'COEF:'
A = coef(X,Y)
print 'A: ', A
print 'EVAL:'
print 't    e^t    p(t)    e^t-p(t)'
maxerror = -1
maxtheor = -1
for i in range(101):
    t = i/100.
    p = eval(A,X,t)
    maxerror = max(maxerror,abs(math.e**t - p))
    error = 1/362880. #1/9!
    error *= math.e**(t)
    for x in X:
        error *= abs(t-x)
    maxtheor = max(maxtheor,error)
    print '%.2f' % t, '%.16f' % math.e**t, '%.16f' % p, '%.16f' % abs(math.e**t - p), error
print 'max absolute error, e^t-p(t):', maxerror
print 'error bound for f(x) with equally spaced interpolation:', maxtheor

print
print '3 ***** Inverse interpolation'
X = [1.9,2.0,2.1,2.2,2.3]
Y = [-1.941,-1.0,0.061,1.248,2.567]
print 'COEF:'
A = coef(Y,X)
print 'A: ', A
print 'EVAL:'
print '%.16f' % eval(A,Y,0.0)
