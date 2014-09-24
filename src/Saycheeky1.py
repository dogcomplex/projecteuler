'''
Created on Aug 23, 2012

@author: W
'''

Bases = [["oh",1],["one",1],["two",1],["three",1],["four",1],["five",1],["six",1],["seven",2],["eight",1],["nine",1],["ten",1],["eleven",3],["twelve",1],["thirteen",2],["fourteen",2],["fifteen",2],["sixteen",2],["seventeen",3],["eighteen",2],["nineteen",2]]

S = ["twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
T = ["hundred","thousand"]
U = [10,1000,1000]
V = [2,2,3,3]
W = [100,1000,1000000,1000000000]

for j in range(2,10):
    for i in range(0,10):
        x = 10*j+i
        s = S[j-2]
        if i>0:
            Bases += [[s+"-"+Bases[i][0],2+Bases[i][1]]]
        else:
            Bases += [[s,2]]
        if s=="seventy":
            Bases[x][1] += 1


    
for j in range(len(T)):
    for k in range(1,U[j]):
        for i in range(W[j]):
            if i==0:
                Bases += [[ Bases[k][0] + " " + T[j], Bases[k][1] + V[j]]]
            else:
                Bases += [[ Bases[k][0] + " " + T[j] + "-" + Bases[i][0], Bases[k][1] + V[j] + Bases[i][1]]]
                          
    print T[j], Bases[W[j]]

    
Mins = []
for i in range(len(Bases)):
    # basic
    b = Bases[i][1]
    
    # 1-concat
    s = str(i)
    sum = 0
    for l in s:
        sum += Bases[int(l)][1]
    if sum < b:
        name = Bases[int(s[0])][0]
        for l in s[1:]:
            name += " " + Bases[int(l)][0]
        #print Bases[i], [name,sum]
        Bases[i] = [name,sum]
    else:
        print "beats 1-concat", Bases[i], i
    
for i in range(len(Bases)):
    print Bases[i][1],
    if i%100==0:
        print
    
    
        
    