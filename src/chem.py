'''
Created on 2011-02-09

@author: Warren
'''
F = []
n = 10
Q = [1,5,4,2,3,1,4,5,6,7]
for j in range(n):
    F.append([])
    for i in range(n):
        if i < j: 
            F[j] += [(Q[i]*Q[j],i,j)]
        elif i > j:
            F[j] += [(-Q[i]*Q[j],i,j)]
print F

