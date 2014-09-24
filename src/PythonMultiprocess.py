import multiprocessing
import time
import random
import sys
from multiprocessing import Process

def f1(x):
    return x**3

def f2(x):
    pass

def f3(x):
    return x

def Queens(col):
    global n, Q, a,b,c
    for row in range(n):
        if a[row] and b[row+col] and c[n+row-col]:
            Q[col] = row
            if col == n-1:
                ''
                #print(Q)
            else:    
                a[row] = b[row+col]=c[n+row-col]=False
                Queens(col+1)
                a[row] = b[row+col]=c[n+row-col]=True
  

      
   
def Queens2((X,n)):
    Q = [0]*n
    a = [True]*n
    b = [True]*(2*n)
    c = [True]*(2*n)

    Q[0]=X
    a[X]=False
    b[X]=False
    c[n+X]=False
    
    def Queens2a(col):
        for row in range(n):
            if a[row] and b[row+col] and c[n+row-col]:
                Q[col] = row
                if col == n-1:
                    ''
                    #print(Q)
                else:    
                    a[row] = b[row+col]=c[n+row-col]=False
                    Queens2a(col+1)
                    a[row] = b[row+col]=c[n+row-col]=True
    
    Queens2a(1)
    

def QueensIt(n):
    Q = [0]*n
    a = [True]*n
    b = [True]*(2*n)
    c = [True]*(2*n)
    
    col = 0
    row = 0
    while col >= 0:
        while row < n:
            #print col, row
            if a[row] and b[row+col] and c[n+row-col]:
                Q[col] = row
                if col == n-1:
                    ''
                    #print Q
                else:    
                    a[row]=b[row+col]=c[n+row-col]=False
                    col +=1
                    row = -1
            row +=1            
        col -=1
        row = Q[col]
        a[row]=b[row+col]=c[n+row-col]=True
        row +=1


def QueensIt2((X,n)):
    Q = [0]*n
    a = [True]*n
    b = [True]*(2*n)
    c = [True]*(2*n)
    
   
    def QueensIt2a(row):
        Q[0]=row
        a[row]=b[row]=c[n+row]=False
        col = 1
        row = 0
        
        while col >= 1:
            while row < n:
                #print col, row
                if a[row] and b[row+col] and c[n+row-col]:
                    Q[col] = row
                    if col == n-1:
                        ''
                        #print Q
                    else:    
                        a[row]=b[row+col]=c[n+row-col]=False
                        col +=1
                        row = -1
                row +=1            
            col -=1
            row = Q[col]
            a[row]=b[row+col]=c[n+row-col]=True
            row +=1  
            
    QueensIt2a(X)


def QueensIt3(col,n,Q,a,b,c):
        
        for row in range(n):
            #print col, row, Q, a, b, c
            if a[row] and b[row+col] and c[n+row-col]:
                Q[col] = row
                if col == n-1:
                    ''
                    #print Q
                else:
                    a[row] = b[row+col]=c[n+row-col]=False
                    if col < 1:  
                        p = Process(target=QueensIt3, args=(col+1,n,Q,a,b,c))
                        p.start()
                    else:
                        QueensIt3(col+1,n,Q,a,b,c)
                    a[row] = b[row+col]=c[n+row-col]=True  
        
if __name__ == '__main__':
    #print tests(4,1000000)

    for n in range(2,17):
        
        Q = [0]*n
        a = [True]*n
        b = [True]*(2*n)
        c = [True]*(2*n)
        '''
        t = time.time()
        Queens(0)
        T=time.time() - t
        
        PROCESSES = n
        pool = multiprocessing.Pool(PROCESSES)
        t = time.time()
        pool.map(Queens2,zip(range(n),[n]*n))
        #pool.join()
        print "Recursive: ",n, time.time() - t
        
        
        t = time.time()
        QueensIt(n)
        T=time.time() - t
        '''
        
        PROCESSES = 10
        pool = multiprocessing.Pool(PROCESSES)
        t = time.time()
        pool.map(QueensIt2,zip(range(n),[n]*n))
        print "Iterative: ",n, time.time() - t 
         
        '''
        Q = [0]*n
        a = [True]*n
        b = [True]*(2*n)
        c = [True]*(2*n)
        
        MAXPROCESSES = 20
        t = time.time()
        QueensIt3(0,n,Q,a,b,c)
        while len(multiprocessing.active_children()) != 0:
            True
        print "SUPER parallel (max 2): ",n, time.time() - t 
        '''
   