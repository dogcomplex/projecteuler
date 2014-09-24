def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

N=20

lcm=1
for i in range(2,N+1):
	lcm = lcm*i**2/gcd(lcm,i**2)


S = list(range(2,N+1))
P = []

goal = lcm/2
for x in S:
	P += [lcm/x**2]
	print lcm/x**2

count =0
def greed(goal,P,i,A):
	if i<0:
		return
	if goal-P[i]==0:
		print A + [i]
	elif goal-P[i]>0:
		greed(goal-P[i],P,i-1,A+[i])
		greed(goal,P,i-1,A)


T = list(reversed(range(1,20)))
greed(100,T,len(T)-1,[])
print "done"


