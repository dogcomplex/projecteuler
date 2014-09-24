'''
Created on Jul 3, 2014

@author: W
'''

'''
from random import *    

class bee:
    def init(self,id):
        self.naive = True
        self.location = 'commitment'
        self.id = id
        self.favored = ''
        self.Prefs = {}
    
    def rate(self,x):
        if self.naive:
            if x in self.Prefs:
                return self.Prefs[x]
            else:
                self.Prefs[x]=random()
                return self.Prefs[x]
        else:
            if x not in self.Prefs:
                self.Prefs[x] = random() 
            return self.strategicrating(x)
    
    def strategicrating(self,x):
        if max(self.Prefs)==x:
            return 1
        else:
            return 0
    
    def pp(self):
        print(self.id, self.location, self.favored)
        
    def go(self,influences):
        t = sum(influences)
        r = random()*t
        for i in influences.keys():
           if r < influences[i]:
               self.location = i
               
    
        
class hive:
    def init(self,n):
        self.Bees = []
        for i in range(n):
            self.Bees = bee(i)
        self.locations = 'commitment'
'''

from random import *
from math import *
        
class bee:
    def __init__(self,i,wait,M,bias,noisesd):
        self.id = i   
        self.location = 0 
        self.wait = wait
        self.defaultwait = wait
        self.bias = bias
        self.preferences = [0]
        self.absent = False
        
        
        for i in range(M):
            r = normalvariate(.5+i*bias,noisesd)
            self.preferences += [(r-.5)]
        self.commitment = 0
         
        
    # note: can't have this on bee side - spoofable    
    def listen(self,Buzz):
        r = random()
        for choice in Buzz.keys():
            if r<=Buzz[choice]:
                return choice
            else:
                r -= Buzz[choice]
        return -1 #no choice made, stay where you are
    
    def waiting(self):
        #bee can control this however it wants
        self.wait -=1
        if self.wait <=0:
            self.wait = self.defaultwait
            return False
        return True
    
    def rate(self,site):
        #naive
        return self.preferences[site]
        #if site >= max(self.preferences):
        #    return 1
        #else:
        #    return 0
        

class hive:
    def __init__(self,size=100,sites=2,search=.1,idle=.05,recruit=.9,assessdelay=3,threshold=.5,printing=True,hardstop=10000,bias=.1,noisesd=.35):
        self.searchchance = search
        self.idlechance = idle
        self.recruitchance = recruit
        self.assessdelay = assessdelay
        self.Sites = []
        self.Bees = []
        self.N = size
        self.M = sites
        self.t = 0
        self.threshold = threshold
        self.printing = printing
        self.idealwinner = ''
        self.actualwinner = ''
        self.hardstop = hardstop
        self.bias = bias

        for i in range(size):
            self.Bees +=[bee(i,self.assessdelay,self.M,bias,noisesd)]
            
        self.Sites +=[size]
        for i in range(1,sites+1):
            self.Sites +=[0]
        
    def addbee(self,b):
        self.Bees += [b]

    def step(self):
        Buzz = {}
        Buzz[0]=self.idlechance
        for i in range(1,self.M+1):
            Buzz[i] = (self.searchchance * 1.0/self.M) + (self.recruitchance * self.Sites[i]*1.0/self.N)
        for b in self.Bees:
            if b.location==0:
                choice = b.listen(Buzz)
                if choice == 0:
                    if b.commitment !=0:
                        self.Sites[b.commitment] -=1
                        self.Sites[0] +=1
                    b.commitment = 0
                    #reset, idle
                elif choice > 0:
                    if choice != b.commitment: 
                        b.location = choice
                        self.Sites[b.commitment] -= 1
                        #remove from active recruiters while scouting new location
            else:
                if not b.waiting():
                    rating = b.rate(b.location)
                    # could do with probability of commitment or with max time commitment...
                    if random() < rating:
                        b.commitment = b.location
                        self.Sites[b.location] +=1
                        b.location = 0
                        # new site wins, return to main nest to recruit for it
                    else:
                        b.location = 0
                        self.Sites[b.commitment] +=1
                        # old site stays, return to main nest to recruit for it
                    
                    
        self.t +=1
                
                                
    def pp(self):
        print self.t, ':',
        for s in self.Sites:
            print s,
        print
    
    def ideals(self): 
        AVGPREFS = [0]*self.M
        for b in self.Bees:
            for m in range(self.M):
                AVGPREFS[m] += b.preferences[m+1]
        for m in range(self.M):
            AVGPREFS[m] /= 1.0*self.N 
        self.idealwinner = AVGPREFS.index(max(AVGPREFS))
        return AVGPREFS
        
    def fullprint(self):
        print self.N, 'agents,', self.M, 'sites;', 'search chance:', self.searchchance, 'idle chance:', self.idlechance, 'recruit chance:', self.recruitchance, 'assessment delay:', self.assessdelay
        
        
        AVGPREFS = self.ideals()
        print 'True Averages: ',
        for m in range(self.M):
            print AVGPREFS[m],
        print
        
        winner = self.winning()
        self.actualwinner = winner
        if AVGPREFS[winner] == max(AVGPREFS):
            
            print 'Correct choice. difference:', AVGPREFS[winner] - max(AVGPREFS[:winner] + AVGPREFS[winner+1:])
            return 1
        else:
            print 'Incorrect choice. difference', AVGPREFS[winner] - max(AVGPREFS[:winner] + AVGPREFS[winner+1:])
            return 0
    
    def winning(self):
        return self.Sites[1:].index( max(self.Sites[1:]))
            
            
        
    def run(self):
        while self.threshold*self.N > max(self.Sites[1:]) and self.t < self.hardstop:
            if self.printing:
                self.pp()
            self.step()
        
        if self.printing:
            self.pp()
            self.fullprint()
        else:
            AVGPREFS = self.ideals()
            self.actualwinner = self.winning()
        
        winner = self.actualwinner
        if self.idealwinner == self.actualwinner:
            return 1, self.t,  abs(AVGPREFS[winner] - max(AVGPREFS[:winner] + AVGPREFS[winner+1:]))
        else:
            return 0, self.t,  abs(AVGPREFS[winner] - max(AVGPREFS[:winner] + AVGPREFS[winner+1:]))
            
            
        
#Queenless

for p in range(10,20):
    
    correctcount = 0
    totaltime = 0
    timefails = 0
    cutoff = 10000
    successdifficulty = 0
    faildifficulty = 0
    tfaildifficulty = 0
    N=100
    
    for i in range(N):
        correct, time, difficulty = hive(100,2,0.1,0.01,.9,0,.35,False,cutoff,0.01*p).run()
        #print correct,time
        if (time < cutoff):
            correctcount +=correct
            totaltime += time
            if correct:
                successdifficulty += difficulty
            else:
                faildifficulty += difficulty
        else:
            timefails +=1
            tfaildifficulty += difficulty
    
    finishes = N-timefails
    if finishes:
        print p
        print 'TOTAL SUCCESSSS:', correctcount*1.0/N*100, '% out of ', N, 'trials'
        print 'accuracy:', correctcount*1.0/finishes*100, correctcount
        print 'time:', totaltime*1.0/finishes, totaltime, 'timefails:', timefails
        if correctcount>0:
            print 'difficulty on successes', successdifficulty*1.0/correctcount, 
        else:
            print 'failed on all completions'
            
        if finishes-correctcount > 0:
            print 'on fail', faildifficulty*1.0/(finishes-correctcount),
        else:
            print 'no failures',
        
        if timefails>0:
            'on time failure', tfaildifficulty*1.0/timefails  
        else:
            print 'no time failures'
            
    else:
        print 'EVERYTHING FAILED.'
        
    print
