N = 500

layers = [1]
for i in range(1,N):
	layers += [3*(i+1)+3*(i-1)]
print layers

sums = [1,7]
for i in range(2,N):
	sums += [sums[i-1] + layers[i]]

print sums

from math import sqrt

ranges = [(0,1)]
for i in range(1,N):
	ranges += [(i*1.5,i*sqrt(3))]

print ranges

for i in range(N):
	if ranges[i][0]<=450 and 450 <=ranges[i][1]:
		print ranges[i]
