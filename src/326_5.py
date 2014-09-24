def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a % b)

'''
Brute force breaker of the relatively prime with difference of three problem (aka the Two Beers problem)
Outputs each x,y that breaks the hypothesis, their gcd, and a list of the augmented x,y pairs to show none are relatively prime 
'''
def twoBeers(limit):
    for y in range(3,limit):
        for x in range(2,y):
            if gcd(x,y)!=1:
                works = True
                for i in range(1,4):
                    if gcd(x,y+i)==1 or gcd(x+i,y)==1:
                        works = False
                if works:
                    print x,y,':', gcd(x,y)
                    for i in range(1,4):
                        print(x,y+i,gcd(x,y+i))
                        print(x+i,y,gcd(x+i,y))
                        
twoBeers(100)
    
'''
Output:
84 90 : 6
(84, 91, 7)
(85, 90, 5)
(84, 92, 4)
(86, 90, 2)
(84, 93, 3)
(87, 90, 3)                        
                        
'''
                