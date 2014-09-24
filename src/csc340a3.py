'''
Created on Feb 2, 2011

@author: Warren Koch
V00482478
'''
from math import *

def f1(x):
    return x**2 - 2.0
def f2(x):
    return x**3 - 2.0*sin(x)
def f3(x):
    return x + 10 - x*cosh(50./x)
def f4(x):
    ''' f(x) = 2sin(2*pi*x) + cos(4*pi*x)
    cos(4*pi*x) = sin^2(2*pi*x) - cos^2(2*pi*x) '''
    return 2*sin(2*pi*x) + cos(2*pi*x)**2 - sin(2*pi*x)**2 
def f5(r):
    ''' given 2 = r*y where r is radius and y is arc angle.
    Using sin(y) = (3/2)/r
    Solve for y: y = 2/r
    sin(2/r) = 1.5/r
    f(r) = 1.5/r - sin(2/r) '''
    return 1.5/r - sin(2./r)

def bisection(a,b,e,f,printit):
    i = 0
    c = a + (b-a)/2.
    while abs(b-a) > 2*e:
        if printit:
            print '%.12f' % c
        if f(a)*f(c)>0:
            a = c
        else:
            b = c
        c = (a+b)/2.0
        i +=1
    return 'Approximation: %.12f' % c, 'Iterations: %d' % i
            
e = 10**-12
print "Bisection: "
print 1, bisection(1,2,e,f1,1)
print
print 2, bisection(0.5,2,e,f2,0)
print 3, bisection(120,130,e,f3,0)
print 4, bisection(0.7,1,e,f4,0)
print 5, bisection(1,2,e,f5,0)

print

def fp1(x):
    return 2.*x
def fp2(x):
    return 3.*x**2. - 2.*cos(x)
def fp3(x):
    return 1. - cosh(50./x) + 50./x *sinh(50./x)
def fp4(x):
    return 4.*pi*cos(2.*pi*x) - 4.*pi*sin(4.*pi*x)
def fp5(r):
    return (2.*cos(2./r)-1.5)/r**2.


''' newton approximation for function f(x) and fp(x) = f'(x) '''
def newtons(x0,e,f,fp):
    x = x0
    i = 0
    do = True
    while do:
        xnext = x - f(x)/fp(x)
        if abs(xnext-x) <= e*abs(x):
            do = False
        print '%.12f' % xnext
        x = xnext
        i+=1
    return 'Approximation: %.12f' % x, 'Iterations: %d' % i


print "Newton:"
e = 10**-12
print 1, newtons(1.5,e,f1,fp1)
print
print 2, newtons(1.25,e,f2,fp2)
print
print 3, newtons(125,e,f3,fp3)
print
print 4, newtons(0.85,e,f4,fp4)
print
print 5, newtons(1.5,e,f5,fp5)
