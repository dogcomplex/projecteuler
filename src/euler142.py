'''
Created on Apr 22, 2013

@author: W
'''
SQUARES = []

for i in range(1,10000):
    SQUARES += [i**2]


def thing():
    x=3
    while True:
        for y in range(x):
            if (x+y)**.5 == int((x+y)**.5) and (x-y)**.5 == int((x-y)**.5):
                for z in range(y):
                    if (x+z)**.5 == int((x+z)**.5) and (x-z)**.5 == int((x-z)**.5):
                        print 'almost', x,y,z
                        if (y+z)**.5 == int((y+z)**.5) and (y-z)**.5 == int((y-z)**.5):
                            print x,y,z
                            return x,y,z
        x +=1


def thing2():
    NEGS = []
    a = 1
    da = 1
    while True:
        b = 1
        db = 1
        while b<a:
            c = a-b
            if c**.5==int(c**.5):
                print a,b,c
                NEGS += [(a,b,c)]
            b += db
            db +=2
        a +=da
        da +=2
        
        
thing2()
            
        