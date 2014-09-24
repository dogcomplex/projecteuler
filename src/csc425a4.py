'''
Created on 2011-03-03

@author: Warren
'''
def secstruct(B):
    n = len(B)
    
    ''' init scores matrix'''
    O = []
    for i in range(n):
        O.append([])
        for j in range(n):
            O[i] += [0]
    
    ''' init t values matrix'''
    T = []
    for i in range(n):
        T.append([])
        for j in range(n):
            T[i] += [[]]
   
    Pairs = {}
    Pairs['C']='G'
    Pairs['G']='C'
    Pairs['U']='A'
    Pairs['A']='U'
   
    def OPT(i,j):
        if i<0 or j>=n or i>=j-4:
            return 0
        if O[i][j] != 0:
            return O[i][j]
        else:
            m = OPT(i,j-1)
            L = []
            for t in range(i,j-4):
                if t<j-4 and Pairs[B[t]]==B[j]:
                    x= 1+OPT(i,t-1)+OPT(t+1,j-1)
                    if x>m:
                        m=x
                        ''' clear the list, fill with new max'''
                        L =[t]
                    elif x==m:
                        ''' add to maximums '''
                        L +=[t]
            T[i][j]=L
            O[i][j]=m
            return m
    
    for i in range(n):
        for j in range(n):
            OPT(i,j)
    return OPT(0,n-1), O, T
        
        
SEQ1 = 'ACCGGUAGU'
SEQ2 = 'ACGUCGAUUCGAGCGAAUCGUAACGAUACGAGCAUAGCGGCUAGAC'
best, O, T = secstruct(SEQ2)
print best
for row in T:
    print row
