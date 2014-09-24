'''
Created on Aug 6, 2012

@author: W
'''
import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))