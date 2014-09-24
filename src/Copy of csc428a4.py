'''
Created on 2011-01-30
CSC428 A2
@author: Warren Koch
V00482478
'''

from struct import unpack

class fasta:
    def __init__ ( self, f ):
        
        l = f.readline()
        if l[0]!='>':
            #Error
            0
        else:
            title = l[1:].rstrip()
            seq = []
            while True:
                l = f.readline().rstrip()
                if not l:
                    break
                else:
                    seq += [l]
            charseq = "".join(seq)
            self.seq = charseq
            self.title = title
        
        # TODO no file, wrongfile exceptions...
        

        '''
        def readint(f):
            return unpack('>L',""+f.read(4))
            
        print f.read(4)
        self.ver = readint(f)
        print self.ver
        self.dbtype = int(unpack('>L',f.read(4)))
        titlelen = int(unpack('>L',f.read(4)))
        #f.read(4) #Empty 32bit field skip
        self.title = unpack('>L',titlelen)
        timestamplen = int(unpack('>L',f.read(4)))
        #f.read(4) #Empty 32bit field skip
        self.timestamp = unpack('>L',timestamplen)
        N = int(unpack('>L',f.read(4)))
        self.N = N
        self.residuecount = int(unpack('<L',f.read(8)))
        self.maxseq = int(unpack('>L',f.read(4)))
        
        self.Hoff = []
        self.Soff = []
        self.Aoff = []
        for i in range(N+1):
            self.Hoff += [int(unpack('>L',f.read(4)))]
        for i in range(N+1):
            self.Soff += [int(unpack('>L',f.read(4)))]
        for i in range(N+1):
            self.Aoff += [int(unpack('>L',f.read(4)))]
        '''
        

ProteinMap = {'-':0, 'A':1}        


''' INFINITY '''
I = float('-inf')

''' returns 2D array of triplets containing sequence alignment scores according to scoring points in inputs '''
def affine(X,Y, match, mismatch, gapstart, gapextend):
    A = []

    for i in range(len(Y)+1):
        A.append([])
        for j in range(len(X)+1):
            A[i].append([I,I,I])
            
            ''' get max score from the left, subject to penalties'''
            if j>0:
                A[i][j][0] = max(A[i][j-1][0] + gapextend, A[i][j-1][1] + gapstart, A[i][j-1][2] + gapstart)
               
            ''' get max score from above, subject to penalties '''
            if i>0:
                A[i][j][2] = max(A[i-1][j][0] + gapstart, A[i-1][j][1] + gapstart, A[i-1][j][2] + gapextend)

            ''' get max score, apply match or mismatch points'''
            if  j>0 and i>0 and Y[i-1] == X[j-1]:
                A[i][j][1] = max(A[i-1][j-1]) + match
            elif j>0 and i>0:
                A[i][j][1] = max(A[i-1][j-1]) + mismatch
            elif j==0 and i==0:
                ''' base case '''
                A[i][j][1] = 0
                
    return A
                

X = "sequence1"
Y = "quincy2"

A = affine(X,Y, 1, -1, -2, 0)


''' print solution '''
print ' ', X
for i,row in enumerate(A):
    if i>0:
        print Y[i-1], row
    else:
        print row
print "Max score: ", max(A[len(Y)][len(X)])

f = open('fasta/spA5DSI2.fasta', 'r')
fast = fasta(f)
print fast.title