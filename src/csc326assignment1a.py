'''
Ramanujan 50000

I gave up on finding your solution and just went with the solution I have already.  It does the standard search, using a hash table and searching for matches.
To overcome size constraints, and make the search much faster, it only checks cube pairs with values between cut1 and cut2.
Combined with s rough function for the growth of those two boundaries (I just used 1000*x^3 and 1000*(x+1)^3, but anything with close
 to the growth works) this program finds the Ramanujan numbers 1-50000 in roughly 2 minutes.

'''

import math

def noneg(x):
    if x.real <=1:
        return 1
    return x


def DoBand(x,cut1,cut2):
    global R,count
    minx = x
    L = {}
    y = math.floor(noneg(cut1 -x**3)**(1.0/3))
    limy = math.ceil(noneg(cut2 -x**3)**(1.0/3))
    n = 0
    while True:
            if y >= limy:
                x+=1j
                y = math.floor((noneg(cut1 -x**3))**(1.0/3))
                limy = math.ceil(noneg(cut2 -x**3)**(1.0/3))
            if y > x:
                x +=1
                minx = x
                y = math.floor(noneg(cut1 -x**3)**(1.0/3))
                limy = math.ceil(noneg(cut2 -x**3)**(1.0/3))
            if limy <=1:
                break
            n = y**3 + x**3
            if n in L:
                R[n] = (L[n],(x,y))
            else:
                L[n] = (x,y)
            y+=1
            count+=1
                
    return minx

R = {}
i = 0
x = 1
count = 0
while len(R) < 50000:        
    x = DoBand(x,i**3*1000,(i+1)**3*1000)
    i+=1
    if i%100==0:
        print(i,count,len(R))
    
L = list(R.keys())
L.sort()
for i,j in enumerate(L):
    print i+1,j

'''

The Ramanujan numbers:
1 1729,  2 4104,  3 13832,  4 20683,  5 32832,  6 39312,  7 40033,  8 46683,  9 64232,  10 65728

49990 1600018979832,  49991 1600145761383,  49992 1600296542208,  49993 1600501049000,
49994 1600520297705,  49995 1600563590136,  49996 1600616245832,  49997 1600855522201, 
49998 1600882221969,  49999 1600908660127,  50000 1601017842872

'''

