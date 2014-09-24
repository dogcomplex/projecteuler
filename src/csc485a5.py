'''
Created on Nov 28, 2011

@author: W
'''

W = [(0,0),(1,0),(2,0)]
B = [(0,2),(1,2),(2,2)]

def printgrid(history):
    global W,B
    for item in history:
        print item, '>',
    print
    for i in range(3):
        for j in range(3):
            if (i,j) in W:
                print 'w',
            if (i,j) in B:
                print 'b',
        print

def move(A,B,colour,history):
    Moves = []
    for i in range(len(A)):
        x,y = W[i]
        if (x,y+1) not in B and (x,y+1) not in A:
            if y+1!=2:    
                Moves += [[colour, (x,y), (x,y+1)]]
        if (x+1,y+1) in B:
            B.remove((x+1,y+1))
            Moves += [[colour, (x,y), (x+1,y+1)]]
        if (x-1,y-1) in B:
            B.remove((x-1,y-1))
            Moves += [[colour, (x,y), (x-1,y-1)]]
    print Moves

                        
        
