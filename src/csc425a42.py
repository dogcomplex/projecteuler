'''
Created on 2011-03-03

@author: Warren
'''

def prettyprint(W,L):
    n = len(W)
    O = []
    for i in range(n):
        O += [-1]
    T = []
    for i in range(n):
        T += [0]
    
    def OPT(i):
        if i >= n:
            return 0
        if O[i]>=0:
            return O[i]
        m = L**2 * n
        len = -1
        k = 0
        while i+k<n and len + 1+W[i+k] <= L:
            len += W[i+k]+1
            x = (L-len)**2 + OPT(i+k+1)
            if x <= m:
                m = x
                T[i]=(i+k,len)
            k +=1
            #print i,k,x,len
        O[i] = m
        return m
    
    return OPT(0), O,T

   


parag = "Call me Ishmael. Some years ago,\
 never mind how long precisely, having little\
 or no money in my purse, and nothing particular\
 to interest me on shore, I thought I would sail\
 about a little and see the watery part of the world"
words = parag.split()
W = []
for word in words:
    W += [len(word)]
print W   
x,O,T = prettyprint(W,38)
print O
print T
i = T[0][0]
while i < len(T)-1:
    print i, words[i], T[i]
    i = T[i][0]