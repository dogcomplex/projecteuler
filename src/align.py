import copy
import sys
import StringIO



class AlignmentException ( Exception ):
    '''
    Represents an exception during alignment.
    '''
    pass



class Grid (object):
    '''
    Represents the edit graph or dynamic programming grid.
    Matrix of cells rows by columns.
    i represents rows and j columns.
    Each cell in the grid contains a Cell object.  
    Alignment specific logic resides in the Cell object.
    A 'stem cell' is used to initialize the grid.  The stem cell is duplicated
    across the grid.
    '''

    def __init__ ( self, stemCell ):
        if stemCell == None:
            raise AlignmentException('Must provide a stem cell.')
        self.stemCell = stemCell
        self.stemCell.grid = self
        # a list of rows
        # 0 is first row and so on
        self._rows = None
        self._top = None
        self._left = None
        self.alignments = set()
        
    def clear ( self ):
        # TODO: make a smarter clear
        self._rows = None
        self._top = None
        self._left = None
        self.alignments.clear()
    
    # type of grid, depends on stem cell
    def gtype ( self ):
        if self.stemCell == None:
            return None
        else:
            return self.stemCell.name()
    
    # align two strings, t and l
    def align ( self, t, l ):
        if self._rows != None:
            raise AlignmentException( 'Must reset prior to alignment.' )
        # initialize
        self._top = t
        self._left = l
        self._rows = []
        for i in range( 0, len(self._left) + 1 ):
            self._rows.append( [] )
            for j in range( 0, len(self._top) + 1 ):
                self._rows[i].append( self.stemCell.duplicate( i, j ) )
        # compute
        for i in range( 0, len(self._left) + 1 ):
            for j in range( 0, len(self._top) + 1 ):
                self._rows[i][j].align()
        # collect alignment string (or strings)
        self._rows[len(self._left)][len(self._top)].collectAlignments( self.alignments )
        return self.alignments

    def cell ( self, i, j ):
        if i < 0 or i >= len(self._rows):
            raise AlignmentException('Cell index i out of bounds ' + str(i))
        if j < 0 or j >= len(self._rows[i]):
            raise AlignmentException('Cell index j out of bounds ' + str(j))
        return self._rows[i][j]
    
    def top ( self, j ):
        if self._top == None:
            raise AlignmentException('Top not set, it is None')
        index = j - 1
        # TODO: return None if j = 0 (index = -1)?
        if index < 0 or index >= len(self._top):
            raise AlignmentException('Index of top out of bounds ' + str(index))
        return self._top[index]

    def size ( self ):
        # size of the matrix
        if self._rows == None or self._rows == []:
            return tuple(0, 0)
        else:
            return (len(self._rows), len(self._rows[0]))

    def left ( self, i ):
        if self._left == None:
            raise AlignmentException('Left not set, it is None')
        index = i - 1
        # TODO: return None if i = 0 (index = -1)?
        if index < 0 or index >= len(self._left):
            raise AlignmentException('Index of left out of bounds ' + str(index))
        return self._left[index]



class Cell (object):
    '''
    Represents a cell in the grid.
    Alignment specific logic resides here.
    Stem cells should be assigned i=-1 and j=-1 (see Grid).
    '''
    
    GAP = '-'
    BACK_UP = 'bUp'
    BACK_LEFT = 'bLeft'
    BACK_DIAG = 'bDiag'
    BACK_MATCH = 'bMat'
    BACK_MISMATCH = 'bMis'
    
    def __init__ ( self, grid, i, j ):
        # cell's location in grid (read-only)
        self.grid = grid
        self.i = i
        self.j = j
        self.score = None
        # back pointers for collecting alignment
        self.backpointers = set()
    
    def name ( self ):
        raise NotImplementedError('')
    
    # Note: do not forget grid duplication.
    def duplicate ( self, i, j ):
        raise NotImplementedError('')
    
    # returns the final alignment score
    def alignmentScore ( self ):
        raise NotImplementedError('')
    
    # this method captures the recurrence
    def align ( self ):
        raise NotImplementedError('')

    # adds alignments to the given set.
    # ex: set(('abc','abc'), ...)
    def collectAlignments ( self, alignments ):
        raise NotImplementedError('')

    # turns the stack 'a' containing symbols into a string
    def _finalize ( self, a ):
        sio = StringIO.StringIO()
        index = len(a) - 1
        while index > -1:
            sio.write( str(a[index]) )
            index -= 1
        string = sio.getvalue()
        sio.close()
        return string



class LCSCell ( Cell ):
    '''
    Longest common sub-sequence with a fixed score of +1 for match and
    0 otherwise.
    Base testing.
    '''
    
    NAME = 'LCS'
    
    def __init__ ( self, grid, i, j ):
        Cell.__init__( self, grid, i, j )
    
    def name ( self ):
        return self.NAME
    
    def duplicate ( self, i, j ):
        return LCSCell( self.grid, i, j )
    
    def alignmentScore ( self ):
        x, y = self.grid.size()
        if x == 0 or y == 0:
            return None
        return self.grid.cell( x-1, y-1 ).score

    def align ( self ):
        if self.i == 0 and self.j == 0:
            self.score = 0
        elif self.i == 0:
            self.score = 0
            self.backpointers.add( self.BACK_LEFT )
        elif self.j == 0:
            self.score = 0
            self.backpointers.add( self.BACK_UP )
        else:
            # i-1,j  (one row less)
            self.score = self.grid.cell( self.i - 1, self.j ).score
            self.backpointers.add( self.BACK_UP )
            # i,j-1 (one column less)
            tmpScore = self.grid.cell( self.i, self.j - 1 ).score
            if self.score == tmpScore:
                # tied score
                self.backpointers.add( self.BACK_LEFT )
            elif tmpScore > self.score:
                # better score
                self.backpointers.clear()
                self.backpointers.add( self.BACK_LEFT )
                self.score = tmpScore
            # i-1,j-1 if vi==wi (diag)
            if self.grid.left( self.i ) == self.grid.top( self.j ):
                tmpScore = self.grid.cell( self.i - 1, self.j - 1 ).score + 1
                if self.score == tmpScore:
                    # tied score
                    self.backpointers.add( self.BACK_DIAG )
                elif tmpScore > self.score:
                    # better score
                    self.backpointers.clear()
                    self.backpointers.add( self.BACK_DIAG )
                    self.score = tmpScore
        #print self.i, self.j, ':', self.backpointers, self.score

    def collectAlignments ( self, alignments ):
        return self._collectA( [], alignments )
    
    def _collectA ( self, a, alignments ):
        if len(self.backpointers) == 0:
            # end; add found alignment
            alignments.add( self._finalize( a ) )
        else:
            # continue collecting
            for bp in self.backpointers:
                if bp == self.BACK_UP:
                    self.grid.cell( self.i - 1, self.j )._collectA( a, alignments )
                elif bp == self.BACK_LEFT:
                    self.grid.cell( self.i, self.j - 1 )._collectA( a, alignments )
                elif bp == self.BACK_DIAG:
                    a.append( self.grid.left( self.i ) )
                    self.grid.cell( self.i - 1, self.j - 1 )._collectA( a, alignments )
                    a.pop()



class AGPCell ( Cell ):
    '''
    Affine gap penalty cell.
    Need to hold a tuple of scores: (sNorth, sWest, sAlign)
    sNorth represents the gap from above.
    sWest represents the gap from the left.
    sAlign represents the diagonal/alignment (or non-gap).
    float('-inf') may not work on all platforms; could cause errors.
    Recurrence on p185 in class text.  Adapted for match and mismatch:
    S_i-1,j-1 + f(v_i,w_j) now has two forms, two conditions.
    '''
    
    NAME = 'AGP'
    N = 0  # north
    W = 1  # west
    D = 2  # diag/align or non-gap
    BACK_UP_NG = 'bUpNG'
    BACK_LEFT_NG = 'bLeftNG'
    
    def __init__ ( self, grid, i, j, match, mismatch, gap, extension ):
        Cell.__init__( self, grid, i, j )
        if match <= mismatch:
            raise AlignmentException('Match is less than or equal to mismatch.')
        if gap < 0 or extension < 0:
            raise AlignmentException('Gap and extension must be greater than 0.')
        # TODO: small waste of mem, fix: refs to shared object
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
        self.extension = extension

    def name ( self ):
        return self.NAME
    
    def duplicate ( self, i, j ):
        return AGPCell( self.grid, i, j, self.match, self.mismatch, self.gap, \
            self.extension )
    
    def alignmentScore ( self ):
        x, y = self.grid.size()
        if x == 0 or y == 0:
            return None
        return self.grid.cell( x-1, y-1 ).score[self.D]

    # compute vertical gap
    # return best, start, extension
    def _computeNorth ( self ):
        x2 = self.grid.cell( self.i-1, self.j ).score[self.N] - self.extension
        x1 = self.grid.cell( self.i-1, self.j ).score[self.D] - (self.gap + self.extension)
        return (max( x1, x2 ), x1, x2)
    
    # compute horizontal gap
    # return best, start, extension
    def _computeWest ( self ):
        x2 = self.grid.cell( self.i, self.j-1 ).score[self.W] - self.extension
        x1 = self.grid.cell( self.i, self.j-1 ).score[self.D] - (self.gap + self.extension)
        return (max( x1, x2 ), x1, x2)

    # implementation of recurrence
    def align ( self ):
        if self.i == 0 and self.j == 0:
            # sNorth and sWest are continuations of a 'long' gap
            self.score = (float('-inf'), float('-inf'), 0)
        elif self.i == 0:
            # sNorth is a continuation of a 'long' gap
            # the best sAlign can do is sWest
            sWest = self._computeWest()[0]
            self.score = (float('-inf'), sWest, sWest) 
            self.backpointers.add( self.BACK_LEFT )
        elif self.j == 0:
            # sWest is a continuation of a 'long' gap
            # the best sAlign can do is sNorth
            sNorth = self._computeNorth()[0]
            self.score = (sNorth, float('-inf'), sNorth)
            self.backpointers.add( self.BACK_UP )
        else:
            # as per the recurrence...
            # compute gap from north
            # compute gap from west
            # compute alignment
            sNorth, ns, ne = self._computeNorth()
            sWest, ws, we = self._computeWest()
            if self.grid.left( self.i ) == self.grid.top( self.j ):
                # match
                sMatch = self.grid.cell( self.i-1, self.j-1 ).score[self.D] + self.match
                sAlign = max( sNorth, sWest, sMatch )
                if sMatch == sAlign:
                    self.backpointers.add( self.BACK_MATCH )
            else:
                # mistmatch
                sMismatch = self.grid.cell( self.i-1, self.j-1 ).score[self.D] + self.mismatch
                sAlign = max( sNorth, sWest, sMismatch )
                if sMismatch == sAlign:
                    self.backpointers.add( self.BACK_MISMATCH )
            # figure out remaining backpointers
            if sNorth == sAlign:
                if sNorth == ns:
                    # start new gap
                    self.backpointers.add( self.BACK_UP_NG )
                else:
                    self.backpointers.add( self.BACK_UP )
            if sWest == sAlign:
                if sWest == ws:
                    # start new gap
                    self.backpointers.add( self.BACK_LEFT_NG )
                else:
                    self.backpointers.add( self.BACK_LEFT )
            # save score
            self.score = (sNorth, sWest, sAlign)
        #print self.i, self.j, ':', self.backpointers, self.score

    def collectAlignments ( self, alignments ):
        return self._collectA( [], [], False, False, alignments )
    
    # of note:
    # during a gap the collector must continue to slide until
    # the gap's start.
    def _collectA ( self, t, l, slidingVert, slidingHori, alignments ):
        if slidingVert and slidingHori:
            raise AlignmentException('Sliding vertically and horizontally.')
        if self.BACK_UP_NG in self.backpointers and self.BACK_UP in self.backpointers:
            raise AlignmentException('Can not start and extend a vertical gap.')
        if self.BACK_LEFT_NG in self.backpointers and self.BACK_LEFT in self.backpointers:
            raise AlignmentException('Can not start and extend a horizontal gap.')
        if self.BACK_MATCH in self.backpointers and self.BACK_MISMATCH in self.backpointers:
            raise AlignmentException('Can not have a match and mismatch.')

        if len(self.backpointers) == 0:
            # end; add found alignment
            pair = (self._finalize( t ), self._finalize( l ))
            alignments.add( pair )
        elif slidingVert:
            # eat left string, gap on top
            l.append( self.grid.left( self.i ) )
            t.append( self.GAP )
            cell = self.grid.cell( self.i-1, self.j )
            if self.BACK_UP_NG in self.backpointers:
                cell._collectA( t, l, False, slidingHori, alignments )
            elif self.BACK_UP in self.backpointers:
                cell._collectA( t, l, True, slidingHori, alignments )
            else:
                raise AlignmentException('Missing up backpointer.')
            l.pop()
            t.pop()
        elif slidingHori:
            # eat top string, gap on left
            l.append( self.GAP )
            t.append( self.grid.top( self.j ) )
            cell = self.grid.cell( self.i, self.j-1 )
            if self.BACK_LEFT_NG in self.backpointers:
                cell._collectA( t, l, slidingVert, False, alignments )
            elif self.BACK_LEFT in self.backpointers:
                cell._collectA( t, l, slidingVert, True, alignments )
            else:
                raise AlignmentException('Missing left backpointer.')
            l.pop()
            t.pop()
        else:
            # continue collecting
            for bp in self.backpointers:
                #print "Handle:", self.i, self.j, bp
                if bp == self.BACK_UP_NG:
                    # eat left string, gap on top
                    l.append( self.grid.left( self.i ) )
                    t.append( self.GAP )
                    self.grid.cell( self.i-1, self.j )._collectA( t, l, False, slidingHori, alignments )
                elif bp == self.BACK_UP:
                    # eat left string, gap on top
                    l.append( self.grid.left( self.i ) )
                    t.append( self.GAP )
                    self.grid.cell( self.i-1, self.j )._collectA( t, l, True, slidingHori, alignments )
                elif bp == self.BACK_LEFT_NG:
                    # eat top string, gap on left
                    l.append( self.GAP )
                    t.append( self.grid.top( self.j ) )
                    self.grid.cell( self.i, self.j-1 )._collectA( t, l, slidingVert, False, alignments )
                elif bp == self.BACK_LEFT:
                    # eat top string, gap on left
                    l.append( self.GAP )
                    t.append( self.grid.top( self.j ) )
                    self.grid.cell( self.i, self.j-1 )._collectA( t, l, slidingVert, True, alignments )
                elif bp == self.BACK_MATCH or bp == self.BACK_MISMATCH:
                    l.append( self.grid.left( self.i ) )
                    t.append( self.grid.top( self.j ) )
                    self.grid.cell( self.i-1, self.j-1 )._collectA( t, l, slidingVert, slidingHori, alignments )
                l.pop()
                t.pop()







# functions options and printing for specific alignments

def runlcs ( s1, s2, options ):
    stemCell = LCSCell( None, -1, -1 )
    grid = Grid( stemCell )
    res = grid.align( s1, s2 )
    print "Results of LCS (score " + str(grid.cell(0,0).alignmentScore()) + "):"
    for s in res:
        print s

def runagp ( s1, s2, options ):
    if options == None or options == '':
        print 'Error in option parameter.'
        return
    try:
        match, mismatch, gap, extension = options.split(',')
        match = float(match)
        mismatch = float(mismatch)
        gap = float(gap)
        extension = float(extension)
    except ValueError:
        print 'Error in option parameter.'
        return
    stemCell = AGPCell( None, -1, -1, match, mismatch, gap, extension )
    grid = Grid( stemCell )
    res = grid.align( s1, s2 )
    print "Results of AGP (score " + str(grid.cell(0,0).alignmentScore()) + "):"
    for t, l in res:
        print t
        print l
        print


# command line interface

# input params: recurence, s1, s2, costs
# costs are dependent on the recurrence

types = { 'lcs':runlcs, 'agp':runagp }

if len(sys.argv) < 4 or len(sys.argv) > 6:
    print 'Computes an alignment between two strings.'
    print 'python', sys.argv[0], ' <type_of_alignment> <string1> <string2> [alignment options as a comma separated string with no spaces]'
    print 'Possible alignments:'
    print 'lcs - longest common subsequence'
    print '  no options'
    print 'agp - affine gap penalty'
    print '  options: cost of match, cost of mismatch, opening gap cost and extension cost'
    print '  example:  1,-1,2,0.5'
    sys.exit(1)

toa = sys.argv[1]
s1 = sys.argv[2]
s2 = sys.argv[3]
options = None
if len(sys.argv) == 5:
    options = sys.argv[4]

if toa not in types:
    print "Unknown alignment."
    print "Possible alignments are:", types.keys()
    sys.exit(1)

types[toa]( s1, s2, options )














