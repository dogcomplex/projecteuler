'''
Tatami
- Made by Warren Koch, V00482478, Sept 28, 2009

Here's how it works.  I stored the board as a word, with every piece as another word situated at position k.
Each possible piece is stored in a List of lists (okay, it should be an array, but Python lists are so easy to use!)
TheBoard is traversed one column at a time, placing a piece then continuing.  The Tatami property is conserved by
assuming all squares besides those along the top and left of the board are invalid initially - only becoming valid
if the square top-left of it is a 1 or 2 (non-unit pieces).  Once BackTrack encounters a spot that violates the 
tatami property, and isn't already occupied (by a horizonal piece placed to the left of it), BackTrack is terminated,
and that branch of the generating tree is cut (since an invalid piece messes everything placed after that anyway).

Sorry for programming it in Python.  But really, speed didn't matter much after the kinks were worked out.
  And I just love this language!
'''


class Piece:
    def __init__(self,height,width,word):
        self.h = height
        self.w = width
        self.word = word

''' Precomputes the pieces, and returns a List of BoardSize length with little 3-length lists of the pieces in word form in relation to position.
  If the piece doesn't fit, an empty word is placed in the list.'''
def BuildPieces(height,width, availablePieces):
        global List, BoardSize, TatamiWarnings
        for i in range(BoardSize):
            
            if i%height != height-1 and i < BoardSize-height:
                TatamiWarnings |= 1<<i
                
            pieces = []
            for piece in availablePieces:               
                if (i%height) + piece.h <= height  and i < BoardSize - (piece.w-1)*height:
                    pieces.append(piece.word<<i)
                else:
                    pieces.append(0)
            List.append(pieces)
            


'''
Tatami: 
'''
def BackTrack(k,pos):
    global BoardSize, TheBoard, List, Solution, UsedUnitMat, BoardAnswer, SolutionCount, TatamiWarnings, CornerCheckConst, Corners, UNITMATMODE
    
    ''' exit if off the board'''
    if k > BoardSize-1:
        return
    
    '''skip over spots with a piece in them already'''
    while pos & TheBoard != 0 and k < BoardSize-1:
        k +=1
        pos = pos<<1
    
    ''' exit if placing a piece would violate Tatami property '''
    if TatamiWarnings & pos != 0:
        return
    
    ''' i=0 for unit mats, i=1 for vertical, i=2 for horizontal. pc is bit representation of each piece'''
    for i, pc in enumerate(List[k]):
        
        ''' if piece not available, skip.  Or, if only one unit mat is allowed, and its used already,
             (or if the board is even, then don't even bother.  SKIP!) '''
        if pc == 0 or ( i == 0 and UNITMATMODE and (BoardSize%2==0 or UsedUnitMat==1)):
            continue 
        
        ''' if piece fits '''
        if TheBoard & pc == 0:
            
            '''add piece'''
            #Solution[k] = i+1
            TheBoard |= pc
            if i == 0:
                if UNITMATMODE:
                    UsedUnitMat = 1 # remove for multi-unit mat problem
            else:
                ''' if a non-unit piece is placed at k, remove the tatami flag at k+CornerCheckConst (i.e. its bottom right
                 corner geometrically)'''
                TatamiWarnings ^= Corners & (pos<<CornerCheckConst)
                
            '''if answer is found, print it, else delve further'''
            if TheBoard == BoardAnswer:
                #print(Solution )
                SolutionCount +=1
            else:
                BackTrack(k+1,pos<<1)
                
            ''' remove piece '''
            if i == 0: #or BoardSize%2==0
                if UNITMATMODE:
                    UsedUnitMat = 0
            else:
                TatamiWarnings ^= Corners & (pos<<CornerCheckConst)
            TheBoard &= ~pc
            #Solution[k] = 0
            
   

''' MAIN '''

for m in range(1,11):
    for n in range(1,m+1): 
        print("=============", m, "x", n, ":")
        
        BoardSize = m*n
        TheBoard = 0 #word
        List = []
        Solution = [0]*BoardSize
        UsedUnitMat = 0
        BoardAnswer = (1<<BoardSize) - 1 #word. = All ones mask
        SolutionCount = 0
        Corners = 0     #word
        CornerCheckConst = m+1
        TatamiWarnings = 0 #word 
        
        ''' Only allow one unit piece (1) or allow unlimited unit pieces (0)? '''
        UNITMATMODE = 1
        
        '''create mats:'''
        pieces = []
        pieces.append(Piece(1,1,1)) 
        pieces.append(Piece(2,1,3))  #vertical mat
        pieces.append(Piece(1,2, 1+(1<<m) )) #horizontal mat
        
        BuildPieces(m,n,pieces)
        TatamiWarnings <<= CornerCheckConst
        Corners = TatamiWarnings
        
        BackTrack(0,1)
        print("Sols = ", SolutionCount)
        
