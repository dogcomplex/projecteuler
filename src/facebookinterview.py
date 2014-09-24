'''
Created on Apr 18, 2013

@author: W
'''
num = "1345686239405409345"
product = 1
for j in range(5):
    product *= int(num[j]) 
max = product
maxi = num[:5]
for i in range(5,len(num)):
    if int(num[i-5])>0:
        newproduct = product*int(num[i])/int(num[i-5])
        if newproduct > max:
            max = newproduct
            maxi = num[i-5:i]
        product = newproduct
        
print max,maxi