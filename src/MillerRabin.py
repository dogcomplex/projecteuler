import math    
import sys
import random

def toBinary(n):
  r = []
  while (n > 0):
    r.append(n % 2)
    n = n / 2
  return r

def test(a, n):
  """
  test(a, n) -> bool Tests whether n is complex.

  Returns:
    - True, if n is complex.
    - False, if n is probably prime.
  """
  b = toBinary(n - 1)
  d = 1
  for i in xrange(len(b) - 1, -1, -1):
    x = d
    d = (d * d) % n
    if d == 1 and x != 1 and x != n - 1:
      return True # Complex
    if b[i] == 1:
      d = (d * a) % n
  if d != 1:
    return True # Complex
  return False # Prime

def MillerRabin(n, s = 50):
  """
    MillerRabin(n, s = 1000) -> bool Checks whether n is prime or not

    Returns:
      - True, if n is probably prime.
      - False, if n is complex.
  """
  for j in xrange(1, s + 1):
    a = random.randint(1, n - 1)
    if (test(a, n)):
      return False # n is complex
  return True # n is prime

   
def concats(n,primes):
    for p in primes:
        if not MillerRabin(int(str(p) + str(n))) or not MillerRabin(int(str(n) + str(p))):
            return False 
    return True

def dfs(V,visits):
    global Edges
    for v in V:
        if v not in visits:
            if concats(v,visits):
                pairs = Edges.get(v,set([]))
                if len(visits) >=3:
                    print visits | set([v])
                dfs(pairs,visits | set([v]))
                Edges[v] = pairs | visits

Primes = [2,3]
Edges = {}
n = 5
max = 0
while max < 5:
    isprime = 1
    for p in Primes:
        if n%p==0:
            isprime = -1
            break
        if p>= int(math.sqrt(n)):
            isprime = 1
            break
    if isprime==1:
        dfs(Primes,set([n]))
        Primes.append(n)
        
                
        #print n, isprime, Edges
        if n%100==0:
            print n, Edges
    n+=1