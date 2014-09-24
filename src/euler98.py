'''
Created on Oct 25, 2011

@author: W
'''

f = open('words.txt', 'r')

line = f.readline()
line = line[1:-1]
W = line.split('","')

WD = {}

for w in W:
    ow = list(w)
    ow.sort()
    ow = "".join(ow)
    if WD.has_key(ow):
        WD[ow] += [w]
    else:
        WD[ow] = [w]

ANA = {}

for k in WD.keys():
    if len(WD[k])>1:
        ANA[k] = WD[k]

print len(ANA), ANA

Squares = []
for i in range(11):
    Squares += [[]]
s = 1
n=1
while s < 10**10:
    Squares[len(str(s))] += [s]
    n+=1
    s = n**2
    
maxi = 0
for words in ANA.values():
    for s in Squares[len(words[0])]:
        n = str(s)

        M = {}
        Values = {}
        fail=False
        for i in range(len(n)):
            M[words[0][i]] = n[i]
            if Values.has_key(n[i]) and Values[n[i]] != words[0][i]:
                fail=True
            else:
                Values[n[i]] = words[0][i]
        if fail:
            continue
        
        newn = ''
        for c in words[1]:
            newn += M[c]
        m = int(newn)
        n = int(n)
        if m!=n and m in Squares[len(words[0])]:
            print words, n,m
            if max(n,m) > maxi:
                maxi = max(n,m)
                print 'MAX', words, n,m, maxi
print maxi
            
    
