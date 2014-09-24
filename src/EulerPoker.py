FACES = ['T','J','Q','K','A']
RANKS = ['A','2','3','4','5','6','7','8','9','T','J','Q','K','A']
SUITS = ['C','S','H','D']
CARDSBYRANK = []
for i,r in enumerate(RANKS):
    CARDSBYRANK.append([])
    for s in SUITS:
        CARDSBYRANK[i].append(r+s)

def rank(x):
    if x[0] == '0':
        return 0
    if x[0] == 'A':
        return 14    
    return RANKS.index(x[0])+1

def unrank(n):
    return RANKS[n-1]  

def highest(H):
    for r in reversed(H):
        if r !=[]:
            return r

def suit(H):
    return H[1]

def groupByRank(H):
    PAIRS = []
    for r in RANKS:
        PAIRS.append(list(set(CARDSBYRANK[rank(r)-1])&set(H)))
    return PAIRS
    
def getStraight(G):
    for i,R in enumerate(reversed(G)):
        if R != []:
            straight = merge(G[9-i:14-i])
            if len(straight) == 5:
                return True,i
            else:
                return False,-1

def getPairs(G):
    pairs = []
    for i,x in enumerate(G):
        if len(x) > 1:
            pairs.append((len(x),i))
    return pairs

def isFlush(H):
    suit = H[0][1]
    for x in H:
        if x[1]!=suit:
            return False
    return True         

def merge(L):
    M = []
    for x in L:
        M.extend(x)
    return M


def getHand(H,G):
    straight,Srank = getStraight(G)
    pairs = getPairs(G)
    pairs.sort()
    #yyyyyyyyyyyyyyyyyyyy
    flush = isFlush(H)
    royal = Srank==13 
    return {'royal':royal,'flush':flush,'Pairs':pairs,'Straight':straight,'Srank':Srank}

def P1Wins(H1,H2):
    G1 = groupByRank(H1)
    G2 = groupByRank(H2)
    
    P1 = getHand(H1,G1)
    P2 = getHand(H2,G2)
    if P1.get('royal') and P1.get('flush'):
        return 1
    if P2.get('royal') and P2.get('flush'):
        return 0
    
    if P1.get('Straight') and P1.get('flush'):
        if P2.get('Straight')&P2.get('flush'):
            if P1.get('Srank')>=P2.get('Srank'):
                return 1
            else:
                return 0
        return 1
    if P2.get('Straight') and P2.get('flush'):
        return 0
    
    if 4 in P1.get('Psizes'):
        if 4 in P2.get('Psizes'):
            P1.get('Pranks')[P1.get('Pranks').index(4)] >= P2.get('Pranks')[P1.get('Pranks').index(4)]:
                return 1
            else
                return 0
        return 1
    if 4 in P2.get('Psizes'):
        return 0
    
    if 3 in P1.get('Psizes'):
        if 3 in P2.get('Psizes'):
            P1.get('Pranks')[P1.get('Pranks').index(3)] >= P2.get('Pranks')[P1.get('Pranks').index(3)]:
                return 1
            else
                return 0
        return 1
    if 3 in P2.get('Psizes'):
        return 0
    
    
    return 0

H1 = ['TC', 'AC', 'KC', 'QC', 'JC']
H2 = ['7D', '2S', '5D', '3S', 'AC']
print (P1Wins(H1,H2))
    