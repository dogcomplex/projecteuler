'''
Snake326.py
Warren Koch
V00482478

This finds a solution to any given Snake sequence (e.g. SSESESESEEEESESEEESEESEEESS ). First it creates a graph representation of the cube,
with edges denoting adjacency. Then it tries starting a sequence at each possible non-isomorphic starting position and direction.  

In x,y,z space, with x horizontal, z vertical, and y forward or back, the following directions are:
+x: right
-x: left
+y: forward
-y: back
+z: up
-z: down

The solution is output in terms of each unit cube's absolute direction away from the previous one, sticking to this orientation.
(Note: since the first piece has no previous piece, its direction is irrelevant)
e.g. "Start (0,0,0) R: RRRFFLLUURDRBBLLUFDDRUUBRFF" denotes a cube that takes the positions 
  (0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0),(1,2,0)...........(2,1,2),(2,2,2)

'''

'''
Builds the cube's big dictionary of association lists (edges). So each point in the cube has a list of points next to it.
'''
def init(n):
    Edges = {}
    for x in range(0,n):
        for y in range(0,n):
            for z in range(0,n):
                es = []
                if x >0:
                    es += [(x-1,y,z)]
                if x < n-1:
                    es += [(x+1,y,z)]
                    
                if y >0:
                    es += [(x,y-1,z)]
                if y < n-1:
                    es += [(x,y+1,z)]
                    
                if z >0:
                    es += [(x,y,z-1)]
                if z < n-1:
                    es += [(x,y,z+1)]
                Edges[(x,y,z)] = es
    return Edges

'''
Moves through the cube space, moving in the same direction as the last recursion if "S", and turning if "E"
'''
def snake(x,y,z,last,k):
    global Edges,Cube, Solution,SOLS,max, maxSol
    
    ''' get difference '''
    (a,b,c) = (x-last[0],y-last[1],z-last[2])
    
    ''' determine direction '''
    dir = 'error'
    if a==1:
        dir = 'R'
    if a==-1:
        dir = 'L'
    if b==1:
        dir = 'F'
    if b==-1:
        dir = 'B'
    if c==1:
        dir = 'U'
    if c==-1:
        dir = 'D'
    
    ''' add current piece to solution set '''
    Cube += [(x,y,z)]
    Solution += [dir]
    
    ''' if we've reached the end '''
    if k==n**3-1:
        SOLS += [''.join(Solution)]
        #print Solution
    else:
        ''' if moving straight, continue in (a,b,c) direction.  But check to see it's a valid move, and hasn't been visited yet '''
        if CONFIG[k]=='S':
            if (x+a,y+b,z+c) not in Cube and x+a in range(n) and y+b in range(n) and z+c in range(n):
                snake(x+a,y+b,z+c,(x,y,z),k+1)
        else:
            ''' 'E': try all possible turns to points we haven't visited yet '''
            Turns = [e for e in Edges[(x,y,z)] if e not in Cube and e not in [(x+a,y+b,z+c),(x-a,y-b,z-c)]]
            for (u,v,w) in Turns:
                snake(u,v,w,(x,y,z),k+1)
    ''' unwind '''
    Solution.pop()
    Cube.pop()


def SnakeStart():
    global Cube, SOLS
    ReturnSols = []    
    
    '''RUN all possible not-obviously-isomorphic starting positions '''
    
    ''' bottom left back corner, facing right '''
    snake(0,0,0,(-1,0,0),0) 
    if SOLS:
        ReturnSols += [("Start (0,0,0) R:",SOLS)]
        SOLS = []
    ''' bottom back center, facing forward '''
    snake(1,0,0,(0,-1,0),0) 
    if SOLS:
        ReturnSols += [("Start (1,0,0) F:",SOLS)]
        SOLS = []
    ''' bottom back center, facing right '''
    snake(1,0,0,(-1,0,0),0) 
    if SOLS:
        ReturnSols += [("Start (1,0,0) R:",SOLS)]
        SOLS = []
    ''' bottom center, facing up '''
    snake(1,1,0,(0,0,-1),0) 
    if SOLS:
        ReturnSols += [("Start (1,1,0) U:",SOLS)]
        SOLS = []
    ''' bottom center, facing right '''
    snake(1,1,0,(-1,0,0),0)
    if SOLS:
        ReturnSols += [("Start (1,1,0) R:",SOLS)]
        SOLS = []
    ''' center, facing right '''
    snake(1,1,1,(-1,0,0),0) 
    if SOLS:
        ReturnSols += [("Start (1,1,1) R:",SOLS)]
        SOLS = []
        
    return ReturnSols


'''
MAIN
'''
n = 3
Edges = init(n)
Cube = []
Solution = []
SOLS = []

config1 = "SSESESESEEEESESEEESEESEEESS"
config2 = "SSESEESEESEEEESESESEESESESS"
config3 = "E"*n**3
CONFIG = config1

SOLS = SnakeStart()

print SOLS

'''
"SSESESESEEEESESEEESEESEEESS" cube:
OUTPUT:
    [('Start (0,0,0) R:', ['RRRFFLLUURDRBBLLUFDDRUUBRFF', 'RRRUULLFFRBRDDLLFUBBRFFDRUU'])]
Eliminate one for isomorphism...
ONE SOLUTION
'''


CONFIG = config3
Cube = []
Solution = []
SOLS = []

SOLS = SnakeStart()

print SOLS

'''
"All Elbows" cube:
OUTPUT:
    []
    
ZERO SOLUTIONS

'''