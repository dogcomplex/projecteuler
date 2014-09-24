f = open('matrix.txt', 'r+')

MATRIX = []
i=0
for line in f:
	MATRIX += [[]]
	for x in line.split(','):
		MATRIX[i] += [x]
	i +=1
print MATRIX

INF = 999999


PATHS = []
	for k in range(n):
		PATHS += [[]]
		for i in range(n):
			PATHS[k] += [[]]
			for j in range(n):
				PATHS[i] += [INF]

for i in range(n):
	for j in range(n):
		PATHS[0]

def FW():
	for k in range(n):
		for i in range(n):
			for j in range(n):


