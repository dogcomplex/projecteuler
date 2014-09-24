import Queue
import threading
import urllib2
import time

class PrimeThread(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue
        
    def run(self):
        while not self.out_queue.empty():
            prime = True
            n = self.out_queue.get()
            for j in range(2,n/2+2):
                if n%j == 0:
                    prime = False
                    #break
            #if prime:
                #print n, "is prime"
            self.out_queue.task_done()

''' 
def threadSerial(threadnum, r):
    #queue = Queue.Queue()
    out_queue = Queue.Queue()

    for i in range(2,r):
        out_queue.put_nowait(i)

    for i in range(threadnum):
        dt = PrimeThread(out_queue)
        dt.setDaemon(True)
        dt.start()

    out_queue.join()
'''  
    
def threadBalanced(threadnum, r):
    start = time.time()
    
    # create queues
    Q = []
    for i in range(threadnum):
        Q.append(Queue.Queue())
        
    # load queues with a (naively) equal distribution of numbers to check
    for i in range(2,r):
        Q[i%threadnum].put_nowait(i)

    # start each thread up
    T = []
    for i in range(threadnum):
        dt = PrimeThread(Q[i%threadnum])
        dt.setDaemon(True)
        dt.start()
        T.append(dt)
        
    while T != []:
        for t in T:
            if not t.isAlive():
                T.remove(t)
              
    return (time.time() - start)
     
    
print "Starting"

x = 100000
iterations = 40

Results = []
Times = []
for threadnum in range(1,20+1):
    sum = 0
    Results.append([])
    for i in range(iterations):
        t = threadBalanced(threadnum,x)  
        print  threadnum, "Threads - Elapsed Time: ",  t
        sum +=t
        Results[threadnum-1].append(t)
    print threadnum, "Threads - Average Time over", iterations, "iterations: ", sum/iterations
    Times += [sum/iterations]

for x in Results:
    print x

for i,x in enumerate(Times):
    print i+1,x
    
    