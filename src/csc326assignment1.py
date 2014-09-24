'''

N = 50000



L = {}
L2 = {}
R = set([])
i = 1
cubes = []
while i < 100:
    i3 = i**3
    cubes.append(i3)
    cut1 = 2*(i-1)**3
    cut2 = (i+1)**3+1
    cut1done = False
    for j3 in cubes:
        n = i3 + j3
        if n <= cut1:
            if n in L:
                R.add(n)
            else:
                L2[n] = "x"
        else:
            if not cut1done:
                L.clear()
                L.update(L2)
                cut1done = True
                
            if n >= cut2:
                L[n] = i3
    i+=1
    print(i,i3,L)
    if i%1000==0:
        print(i)


Ramanujans = list(R)
Ramanujans.sort()
print( len(Ramanujans),Ramanujans)
'''

import math

R = {}
def noneg(x):
    if x<=1:
        return 1
    return x


def DoBand(x,cut1,cut2):
    global R
    #waste = 0
    count = 0
    minx = x
    L = {}
    y = math.floor(noneg(cut1 -x**3)**(1.0/3))
    limy = math.ceil(noneg(cut2 -x**3)**(1.0/3))
    n = 0
    while True:
            if y >= limy:
                x+=1
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
            #print(x,y,minx,limy,n)
            if n in L:
                #print(cut1, count, n, cut2)
                R[n] = (L[n],(x,y))
            else:
                L[n] = (x,y)
            y+=1
            
            count+=1
            #if n < cut1 or n >= cut2:
            #    waste +=1

    
    #if waste > 0:
        #print(cut1, waste, cut2)
    return minx
    #print(x,y,n)
    #print(R)
    #print(len(L),cut1,cut2, L)
    #print(len(L),len(R))
  
  
i = 0
x = 1
while len(R) <= 50000:            
    x = DoBand(x,i**3*1000,(i+1)**3*1000)
    i+=1
    if i%100==0:
        print(i,len(R))
    
#print(len(R),R)
L = list(R.keys())
L.sort()
for i,j in enumerate(L):
    print(i+1,j, end=",  ")

'''

The Ramanujan numbers:
1 1729,  2 4104,  3 13832,  4 20683,  5 32832,  6 39312,  7 40033,  8 46683,  9 64232,  10 65728

49990 1600018979832,  49991 1600145761383,  49992 1600296542208,  49993 1600501049000,
49994 1600520297705,  49995 1600563590136,  49996 1600616245832,  49997 1600855522201, 
49998 1600882221969,  49999 1600908660127,  50000 1601017842872
'''

