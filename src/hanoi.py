
sum = 0
N = 1000
N -=1
for k in [3,5]:
    n = N/k #floor
    sum += k*n*(n+1)/2
LCD = []    
for k in LCD:
    n = N/k #floor
    sum -= k*n*(n+1)/2
print sum