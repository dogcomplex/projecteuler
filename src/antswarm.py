'''
    Created on Nov 16, 2011
    
    @author: W


'''
from random import random
import threading
from copy import copy
import math



class site:
    global sitelist,n
    id = 0
    # search probability from site
    SPFS = None
    # search distance from site
    #SDFS = None
    # recruit probability from site
    RPFS = None
    ants = None
    avgscore = 0
    scorecount = 0
    trueavg = 0
    
    recruits = 0
    finds = 0
    decay = 0
    newbs = 0
    
    def __init__(self,id,SPFS,RPFS):
        self.id = id
        self.SPFS = copy(SPFS)                
        self.RPFS = copy(RPFS)
        self.ants = []
    def printsite(self):
        print "site ", self.id,  len(self.ants), '(+', self.recruits, '+', self.finds, '-', self.decay, ') =', self.newbs, "[",
        for ant in self.ants:
            print ant.id,
        print "]"
        print '=', self.trueavg, '~', self.avgscore, self.scorecount

class ant(threading.Thread):
    
    
    id = -1
    prefsite = None
    prefstrength = 0
    SitePrefs = []
    recruitcall = None
    quota = 0
    tick = 1
    delay = 0

    
    def __init__(self,id,start,prefs):
        threading.Thread.__init__(self)
        self.id = id
        self.prefsite = start
        start.ants.append(self)
        self.SitePrefs = copy(prefs)

    def run(self):
        #global object view
        global antlist, sitelist, home
        #global constants
        global n, searchchance, qthreshold, quorumfound, decayrate
        #global threading vars
        global tock, antsready, ready, qantsready
        #global thread lists
        global jointhreads
        
        ready.acquire()
        while self.tick-self.delay >= tock:
            if antsready==n-1:
                antsready=0
                tock += 1
                ready.notify_all()
                print "ROUND ", tock
                for site in sitelist:
                    site.printsite()
                    site.recruits = 0
                    site.newbs = 0
                    site.finds = 0
                    site.decay=0
            else:
                antsready +=1
                ready.wait()
            
            if quorumfound:
                if jointhreads:
                    jointhreads[0].join()
                jointhreads += [self]
                print "QUORUM FOUND SITE", quorumfound.id
                for site in sitelist:
                    site.printsite()   
                ready.release()
                          
        if self.quorumcheck():
            #begin carrying
            quorumfound = self.prefsite
        if self.recruitcall:
            self.recruitcall.recruits +=1
            self.assess(self.recruitcall)
        rnd = random()
        if rnd <= decayrate:
            self.quota = 0
            self.prefsite.decay +=1
            self.prefsite.newbs -=1
            self.move(home)
        if self.quota > 0:
            self.quota -=1
            self.recruit()
        elif searchchance():
            self.search()
        self.tick += 1
        self.run()
        

    def quorumcheck(self):
        if self.prefsite.id != home.id:
            return len(self.prefsite.ants) >= qthreshold
        return False

    def search(self):
        rnd = random()
        x = 0.
        i = 0
        while rnd > x and i < sitecount+1:
            x += self.prefsite.SPFS[i]
            i += 1
        choice = i-1
        # delay?
        if choice!=self.prefsite.id:
            #ant moves here
            sitelist[choice].finds +=1
            self.assess(sitelist[choice])
        
    def move(self, newsite):
        self.prefsite.ants.remove(self)
        newsite.ants.append(self)
        self.prefsite = newsite
    
    def assess(self,new):
        self.recruitcall = None
        newscore = self.SitePrefs[new.id]
        new.avgscore = (new.avgscore*new.scorecount + newscore)/(new.scorecount+1)
        new.scorecount += 1

        if assesschance(newscore):
            self.move(new)
            new.newbs +=1
            #recruit
            newsitecount = len(new.ants)
            self.quota =0
            for i in range(n-newsitecount):
                if recruitchance(newscore):
                    self.quota +=1
        self.recruitcall = None
    
    def recruit(self):    
        L = []
        for a in antlist:
            if a.recruitcall == None and a.prefsite.id != self.prefsite.id:
                L += [a]
        if L:
            rnd = int(random()*len(L))
            a = L[rnd]
            a.recruitcall = self.prefsite
                




#MAIN
n = 100

#note: site 0 is home
sitecount = 2

# decay k
decayrate = 0.01

qthreshold = int(n*.4)
quorumfound = None

def recruitchance(score):
    rnd = random()
    recruitfactor = 1
    if rnd < recruitfactor*score:
        return True
    else:
        return False
    
def assesschance(score):
    rnd = random()
    acceptfactor = 1
    if rnd < acceptfactor*score:
        return True
    else:
        return False
    
def searchchance():
    rnd = random()
    searchfactor = .05
    if rnd < searchfactor:
        return True
    else:
        return False

# populate this properly
# assume adds to 100%, else adds to decay
SPFSmatrix = []
RPFSmatrix = []
'''
for i in range(sitecount+1):
    SPFSmatrix += [[]]
    RPFSmatrix += [[]]
    for j in range(sitecount+1):
        if i==0:
            if j==0:
                SPFSmatrix[i] += [searchdecay]
                RPFSmatrix[i] += [0]
            else:
                SPFSmatrix[i] += [(1.-searchdecay)/sitecount]
                RPFSmatrix[i] += [1./sitecount]
        elif i==j:
            SPFSmatrix[i] += [0]
            RPFSmatrix[i] += [0]
        else:
            if j==0:
                SPFSmatrix[i] += [0]
                RPFSmatrix[i] += [1./sitecount]
            else:
                SPFSmatrix[i] += [(1.-searchdecay)/(sitecount-1)]
                RPFSmatrix[i] += [1./sitecount]
'''
'''TODO: check this again.  scrap stupid searchdecay and add a constant decay factor? '''
SPFSmatrix = [[0,.5,.5],[0,0,1],[0,1,0]]        
RPFSmatrix = [[0,0,0],[.5,0,.5],[.5,.5,0]]       
     
sitelist = []
for i in range(sitecount+1):
    sitelist += [site(i,SPFSmatrix[i],RPFSmatrix[i])]


antsready = 0
ready = threading.Condition()
qantsready = 0
home = sitelist[0]
antlist = []
jointhreads = []
tock = 0
AVGS = [0]*(sitecount+1)
for i in range(n):
    x = random()
    Prefs = [0,x,x*.9]
    antlist += [ant(i,home,Prefs)]
    for j in range(len(AVGS)):
        AVGS[j] += Prefs[j]
for j in range(len(AVGS)):
        sitelist[j].trueavg = AVGS[j]/n

        
print "running"
for i in range(n):
    antlist[i].start()

ready.acquire()    
while not quorumfound:
    ready.wait()
    

    