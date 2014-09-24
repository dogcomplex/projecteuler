from copy import copy

N=15
Worlds = [[1,1,[1,0,0,0,0],1,0]]
for rounds in range(N):
	nextworlds = []
	for [n,d,A,sum,times] in Worlds:
		for i in range(5):
			if A[i] !=0:		
				Ax = copy(A)
				Ax[i]-=1
				for j in range(i+1,5):
					Ax[j]+=1
				if sum==1 and rounds!=0:
					times +=1
					print rounds,n,d,A,sum,times
				w = [n*A[i],d*sum,Ax,sum+(3-i),times]
				nextworlds += [w]
	Worlds = nextworlds
	print len(Worlds)
total = 0
for [n,d,A,sum,times] in Worlds:
	total += n*(times)*1./d

print total


