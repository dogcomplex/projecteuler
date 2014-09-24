'''
Created on Sep 2, 2012

@author: W
'''
f = open('network.txt', 'r')

E = {}
n=40
for i in range(n):
    E[i] = {}

i=0
for line in f:
    j=0
    for s in line.split(','):
        if s!='-' and s!='-\n':
            E[i][j] =int(s)
            E[j][i] =int(s)
        j+=1
    i+=1 

x = 0
U = [x]
Enew = []
while len(U)<n:
    X = []
    m = (1000000000,-1,-1)
    for x in U:
        for y in E[x].keys():
            if y not in U:
                if E[x][y]< m[0]:
                    m = (E[x][y],x,y) 

    U +=[m[2]]
    Enew += [m]

print U, Enew

    
