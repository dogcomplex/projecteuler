'''
Created on Apr 4, 2012

@author: W
'''
import random
random.seed(2)

P = []
n=100
m=5
threshold = n/2
T = 100


means = []
for j in range(m):
    P += [[]]
    means += [0]
    for i in range(n):
        P[j] += [random.random()]
        means[j] = (means[j]*i + P[j][i])/(i+1)
print P
print means

maxmean = max(means)
minmean = min(means)
correctchoice = means.index(maxmean)

random.seed(None)
    
    
wincount = 0
losecount = 0
trials = []
counts = [0]*m
solomean = 0
for k in range(T):
    Winners = []
    for j in range(m):
        count = 0
        for i in range(n):
            if P[j][i] >= random.random():
                count +=1
        if count >= threshold:
            Winners += [j]
        
    if correctchoice in Winners:
        if Winners ==[correctchoice]: 
            wincount +=1
            solomean +=means[correctchoice]
    elif len(Winners)==1:
        losecount +=1
        solomean +=means[Winners[0]]
    trials += [Winners]
    for i in Winners:
        counts[i] +=1

solomean /= wincount+losecount
print wincount, losecount, wincount*1./T, losecount*1./T, maxmean/minmean, minmean/maxmean, wincount*1./losecount, losecount*1./wincount
print trials
print counts
meanmean = 0
for i in means:
    meanmean += i
meanmean /= len(means)
resultavg = 0
total = 0
for i,x in enumerate(counts):
    resultavg += x*means[i]
    total += x
    print x, means[i], x/means[i]
resultavg /= total
print total, meanmean, solomean, abs(meanmean - solomean), resultavg, abs(meanmean - resultavg)