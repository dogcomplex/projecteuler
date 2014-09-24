'''
Created on 2011-01-30
CSC428 A2
@author: Warren Koch
V00482478
'''

from struct import unpack

class fasta:
    def parsetitle(self, T):
        #TODO
        return T
    
    def __init__ ( self, f ):
        l = f.readline()
        if l[0]!='>':
            #Incorrect formating error
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
            self.title = self.parsetitle(title)
        
class AlignMatrix:
    def __init__ ( self, file ):
        line = file.readline()
        while line and line[0]=='#':
            line = file.readline()
        #TODO: no line error
        
        Rows = {}
        COLS = line.split()
        n = len(COLS)
        self.values = []
        for c in COLS:
            self.values += [c]
            Rows[c] = {}
        
        line = file.readline()
        while line:
            if line[0]!='#':
                row = line.split()
                r = row[0]
                print r, c,  n, len(row), row
                for j in range(n):
                    c = COLS[j]
                    Rows[r][c] = int(row[j+1])
            line = file.readline()

        self.Score = Rows
        
            
        
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


blosumf = open('blosum62.txt', 'r')
B = AlignMatrix(blosumf)
