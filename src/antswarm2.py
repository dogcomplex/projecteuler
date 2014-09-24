
from random import *
import math

def printit(L):
    for i in L:
        print i, '\t',
    print


def antswarm(n,m,k,quorum, q, r,Qnoise, Rnoise, Crate,bdr,brr,nonegs,directswitch,qrcorrelation,jerks,biasedjerks,w,noisesd):
    CUTTOFF = 100
        
    def Q(i):
        basediscoveryrate = bdr
        rnd = normalvariate(.5,noisesd)
        return basediscoveryrate *(q[i]) + Crate*Qnoise[i]*(rnd-.5) + qrcorrelation*(R(i))

    def R(i):
        
        baserecruitrate = brr
        rnd = random()
        rnd2 = random()
        if rnd2 < jerks:
            if rnd2 < biasedjerks:
                if i==0:
                    return 0
                else:
                    return baserecruitrate
            else: 
                return baserecruitrate*(round(r[i] + Crate*Rnoise[i]*(rnd-.5)))
        else:
            return baserecruitrate *(r[i]) + Crate*Rnoise[i]*(rnd-.5) 
    
    
    t=0
    s = n
    s2 = 0
    Y = [0]*m
    Y2 = [0]*m 
    quorumfound = 0
    
    
    while not quorumfound and t< CUTTOFF:
        s2 = s
        for i in range(m):
            
            wanderers = s*Q(i)
            homerecruits = Y[i]*s*R(i) 
                
            leakage = k*Y[i]
            
            if nonegs:
                ds = max(- homerecruits - wanderers + leakage,-s2)
                dy = max(homerecruits + wanderers - leakage,Y[i])
                dd = min(-ds,dy)
                
                Y2[i] = Y[i] + dd
                s2 = s2 - dd
            else:
                Y2[i] = Y[i] + homerecruits + wanderers - leakage
                s2 = s2 - homerecruits - wanderers + leakage
            
            if directswitch:
                for j in range(m):
                    if i!=j:
                        if nonegs:
                            recruits = w*min(Y[i]*Y[j]*R(i),Y[j])
                        else:
                            recruits = w*Y[i]*Y[j]*R(i)
                            
                        Y2[i] += recruits
                        Y2[j] -= recruits
            
        s = s2
        s2 = 0
        
        sum = s
        for i in range(m):
            sum += Y2[i]
            Y[i] = Y2[i]
            Y2[i] = 0
            
        if sum !=0:
            s /=sum
            for i in range(m):
                Y[i] /= sum
                if Y[i]>quorum:
                    quorumfound = [i]
            
        t +=1
    
    if t<CUTTOFF:
        return quorumfound, t, s, Y
    else:
        return [-1], t, s, Y

           
n = 1000
m = 2 
k = 0.1 #idle - 0 to .2 
its = 1000
bdr = .05 #discovery rate - keep low as possible
brr = 1 #recruitment rate -  .4 onward 
quorum = .35 #.35 - .6 is good
C = .1 # under .2 ish - noise rate?
qrcorr = 0.2 #.2 onward
jerks = 0 # best 0, works up til like 70%
biasedjerks = 0 # linearly reduces to just random around 50%. Nice.
sd = .35
diff = 0
qdiff = 0
qndiff=1
rndiff=1
w = 1
noisesd = .01

X = []
for i in range(0,100):
    X += [i*.01]

L = []
for i in range(0,1):
    L += [i*.01]


for bdr in X:
    for d in L:
        
        err = 0
        timeouts = 0
        avgt = 0
        for i in range(its):
            q = []
            r = []
            for i in range(m):
                rnd = random()
                q = [random(), random()]
                rnd = random()
                Qnoise = [rnd,rnd*qndiff]
                #q +=[.5 + qdiff*(random()-.5)]
                rnd = random()
                r = [random(),random()]
                Rnoise = [rnd,rnd*rndiff]
            correct = r.index(max(r))
            penalty = abs(r[0]-r[1])
            qu,t,s,Y = antswarm(n,m,k,quorum,q,r,Qnoise,Rnoise,C,.1*bdr,brr,False,True,qrcorr,jerks,biasedjerks,w,noisesd)
            #print quorum, qu, t, s, Y, q
            if qu[0]<0:
                timeouts +=1
            else:
                if qu[0] != correct:
                    err +=penalty
                avgt += t
                
        if timeouts != its:
            printit([.1*bdr,k, err*1./(its-timeouts), timeouts*1./its, (err + timeouts)*1./its, avgt/(its-timeouts)])
        else:
            printit([bdr,k, 0, 1, 1, 1000])