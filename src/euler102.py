'''
Created on Aug 5, 2012

@author: W
'''
f = open('triangles.txt', 'r')

class point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

def ccw(A,B,C):
    return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)
def intersect(A,B,C,D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
def lintersect(l1,l2):
    return intersect(l1[0],l1[1],l2[0],l2[1])

ORIGIN = [point(0,0),point(0,100000)]

insidecount =0

for line in f:
    P = line.strip().split(',')
    points = []
    for i in range(3):
        points += [point(int(P[2*i]),int(P[2*i+1]))]
    edges = []
    count = 0
    for i in range(3):
        edges += [(points[i],points[(i+1)%3])]
        if not lintersect(ORIGIN,edges[i]):
            print line
            count +=1
    if count%2==0:
        insidecount +=1
print insidecount