#Project Euler Problem 3
#4/13/2012
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

import math

nump = 600851475143
num = nump

half = math.floor(num/2)
print half

max = 0
factors=[]
i=1
tempproduct = 1


while i<=half:
    if (num%i==0):
        print i
        factors.append(i)
        num=num/i
        half = math.floor(num/2)
        tempproduct = tempproduct*i
    i=i+1


print tempproduct
factors.append(nump/tempproduct)
print factors

factors_prime = []

for j in factors:
    prime = 1
    i=2
    temp = math.floor(j/2)
    while ((prime == 1) and (i<=temp)):
        if (j%i)==0:
            prime = 0
        i=i+1
    factors_prime.append(prime)

