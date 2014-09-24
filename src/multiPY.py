from multiprocessing import *
import time

def f(n):
    for i in range(2,n/2+2):
        if n%i == 0:
            return False
    return True

if __name__ == '__main__':
    
   
    numthreads = 20
    size = 100000
    iterations = 5
    
    Results = []
    Avgs = []
    for t in range(1,numthreads+1):
        sum = 0
        Results.append([])
        for i in range(iterations):
            start = time.time()
            
            # Do real threading work here
            pool = Pool(processes=t)
            pool.map(f, range(2,size))
            
            # end of threading work
            timetaken = time.time() - start
            sum +=timetaken
            Results[t-1].append(timetaken)
            print t, timetaken
        print "avg:", t, sum/iterations
        Avgs +=[sum/iterations]
        
    print ""
        
    for i,x in enumerate(Results):
        print x 
    
    print ""
    print "averages:"
    print ""
    
    for i,x in enumerate(Avgs):
        print i+1,x 
    