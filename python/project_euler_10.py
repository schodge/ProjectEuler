# Project Euler Problem 10
# 3/18/2013
# Copyright Shayne Hodge
# Find the sum of all the primes below two million.

import numpy

def sieve(start):
    if (start == 2):
        k = 2
        while (((k*start)-offset) <= (isprimelen-1)):
            isprime[(k*start) - offset] = 0
            k += 1
        return
    k = 3
    while (((k*start)-offset) <= (isprimelen-1)):
        isprime[(k*start) - offset] = 0
        k += 2
    return

def nextvalue(lastvalue):
    iindex = lastvalue - offset + 2
    while (iindex <= (end_value-offset)):
        if isprime[iindex] == 1:
            return (iindex + offset)
        else:
            iindex += 2
    return (end_value+1)

end_value = 2*10**6 - 1
sievelist = numpy.array(range(2, end_value+1),dtype='int64')
offset = sievelist[0]
isprime = numpy.array([1] * (end_value + 1 - offset),dtype='int64')
isprimelen = len(isprime)

sieve(2)
sieve(3)
knownprime = 5

while (knownprime <= end_value):
    sieve(knownprime)
    knownprime = nextvalue(knownprime)    
    
primesum = sum(sievelist*isprime)

print('The sum of all primes less than', end_value+1, 'is', primesum, '.')
