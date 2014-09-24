'''
Created on May 28, 2014

@author: W
'''


'''
D = {}
D[1]=[(0,set([1]))]

Mins = {}
Mins[1] = [(0,set([1]))]

import math

for n in range(2,201):
    
    D[n] = []
    for j in range(1,n/2+1):
        for size1,S1 in D[j]:
            for size2,S2 in D[n-j]:
                D[n] += [(max(size1,size2)+1, S1.union(S2).union(set([n])))]
    
    Removals = []
    i =0
    print n,len(D[n]),
    while i < len(D[n]):
        for j in range(len(D[n])):
            if i!=j:
                if D[n][i][1].issubset(D[n][j][1]):
                    if D[n][i][0] >= D[n][j][0]:
                        #print n, D[n][i],D[n][j]
                        D[n].pop(i)
                        i-=1
                        break
        i +=1
    minsize = 1000000000
    minset = set([])
    for i in range(len(D[n])):
        if minsize > D[n][i][0]:
            minsize = D[n][i][0]
            minset = D[n][i][1]
    print len(D[n]),
    print minsize,minset
    
    D[n] = []
    Mins[n] = []
    for j in range(1,n/2+1):
        for size1,S1 in Mins[j]:
            for size2,S2 in Mins[n-j]:
                #print n, S1.difference(S2).difference(set([n,n-j]))
                steps = 0
                needs = S1.difference(S2).difference(set([n,n-j]))
                while needs:
                    x = needs.pop()
                    steps += Mins[x][0][0]
                    needs = needs.difference( Mins[x][0][1])
                D[n] += [(max(size1,size2)+1+steps, S1.union(S2).union(set([n])))]
                
                steps = 0
                needs = S2.difference(S1).difference(set([n,n-j]))
                while needs:
                    x = needs.pop()
                    steps += Mins[x][0][0]
                    needs = needs.difference( Mins[x][0][1])
                D[n] += [(max(size1,size2)+1+steps, S1.union(S2).union(set([n])))]
                
                
                
    if D[n] == []:
        print 'uhon'
        break
    minsize = 1000000000
    minsets = []
    minsetsize = 0
    for i in range(len(D[n])):
        if minsize > D[n][i][0]:
            minsize = D[n][i][0]
            minsets = [D[n][i][1]]
        
        if minsize == D[n][i][0]:
            if len(D[n][i][1]) < minsetsize:
                minsets += [D[n][i][1]]
                maxsetsize = len(D[n][i][1])
                

            
            distinct = True
            
            for S in minsets:
                
                    
                
                if D[n][i][1].issuperset(S):
                    S = D[n][i][1]
                    distinct = False
                elif S.issuperset(D[n][i][1]):
                    distinct = False
            if distinct:
                minsets += [D[n][i][1]]
          
    
    for S in minsets: 
        Mins[n] += [(minsize,S)]
    print n,Mins[n]
        

sum=0
for i in range(1,201):
    sum += Mins[i][0][0]
print sum

'''

D = {}
D[2] = [1]
D[3] = [2]
D[4] = [3,2]
D[5] = [4,3]
D[6] = [5,4,3]

Min = {}
Min[1] = 0
Min[2] = 1
Min[3] = 2

import math
N = 200
for n in range(1,N+1):
    D[n] = list(range(int(math.ceil(n/2.0)),n))

print D

for n in range(1,N+1):
    

'''
D[6] = 5,4,3
5 = 4,3
4 = 3,2 , 1
3 = 2 , 2 = 1
2 = 1
min = 5
4 = 2, 2
2 = 1
min = 4
5 = 3, 2
3 = 2, 2 = 1
2 = 1
min still 4
6 = 4 , 2
4 = 3, 2 = 1
3 = 2
2 = 1
min still 4
6 = 3, 3
3 = 2, 3 = 2
2 = 1
min 3

return 4

power comes from updating min as you go
if you can beat the min, do it
if not, break

'''
    
def mintry(n,x,min,c,L):
    if c > min:
        return -1
    count = 0
    for a in D[x]:
        mintry(n,a,min,c+1,)
        