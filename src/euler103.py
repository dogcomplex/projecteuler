'''
Created on Aug 6, 2012

@author: W
'''

import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

S = [1,2,3,4]
print findsubsets(S,4)

def isspecial2(S):
    for ss in findsubsets(S,len(S)):
        kjklj
    