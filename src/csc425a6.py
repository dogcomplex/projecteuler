'''
Created on 2011-04-01

@author: Warren Koch
V00482478
'''

from math import *


INF = 10**7
''' convert file to variables and lists '''
def readknap(f):
    n = int(f.readline())
    W = []
    V = []
    vmax = 0
    for i in range(n):
        Line = f.readline().split()
        W += [int(Line[1])]
        v = int(Line[2])
        vmax = max(vmax,v)
        V += [v]
    totalw = int(f.readline())
    return n,W,V,totalw,vmax

''' compute OPT(n) = max value < total weight where i=n '''
def OPTI(n,maxweight,V,W):
    ''' init: Dictionary with Value as keys and a tuple containing Total Weight and the list of current items as values.
    i=0:  L[0] has weight 0 with empty list, all others have infinite (and so aren't included)
    '''
    L = {}
    L[0]=[0,[]]
    vmax = 0
    for i in range(n):
        ''' create dummy dictionary for the next round to ensure no item is added twice '''
        D = {}
        for v in L.keys():
            ''' if it fits weight restrictions '''
            if L[v][0] + W[i] <= maxweight:
                ''' if it's not in the dictionary yet, or it's smaller than the current weight '''
                if not D.has_key(v + V[i]) or D[v + V[i]][0] > L[v][0]+W[i]:
                    D[v + V[i]] = [0,[]]
                    ''' update total weight '''
                    D[v + V[i]][0]=L[v][0] + W[i]
                    ''' update list (nested reference)'''
                    D[v + V[i]][1]=[L[v][1],i]
                    
                    vmax = max(vmax, v+V[i])
        ''' merge next row with previous '''
        for v in D.keys():
            if not L.has_key(v) or L[v][0] > D[v][0]:
                L[v] = D[v]
    return vmax,L[vmax][0],L[vmax][1]            
               

''' compute the Epsilon-Approximation max value for a knapsack with maximum weight '''
def PTASKnap(f,eps):
    n,W,V,totalw,vmax = readknap(f)
    scale = eps*1.0 * vmax / n
    '''reduce by scaling factor:'''
    Vhat = []
    for v in V:
        Vhat += [int(ceil(v/scale))]
    v,w,L = OPTI(n,totalw,Vhat,W)
    
    
    ''' unpack nested list, add up the actual value of items'''
    Items = []
    vactual = 0
    while len(L)>0:
        Items += [L[1]]
        vactual += V[L[1]]
        L = L[0]
    Items.sort()
      
    
    print "Epsilon ", eps," approximate maximum list for weight of ", totalw, ": "
    print "total approximate value:", v*scale, " ~= ", int(floor(v*scale))
    print "total actual value:", vactual 
    print "total weight:", w
    print "Items:", Items
    print


'''MAIN'''
Files = ["knapsack20.txt","knapsack10x.txt","knapsack100x.txt", "knapsack1000x.txt"]
for file in Files:
    print file, " :"
    for eps in [1/2.,1/10.,1/50.]:
        f = open(file,'r')
        PTASKnap(f,eps)

