# Project Euler Problem 7
# 5/11/2012 - 3/14/2013
# Copyright Shayne Hodge
# Find the 10,001st prime


# first primes are 2,3,5,7,11,13,17,19,23...
# 2 is prime, but then 2n is not prime for all n>1
# so list from 2 to end_value
# seperate list, isprime, set at 1 for length(end_value)
# set all the 2n's to zero
# find the next value for which isprime == 1
# repeat

def sieve(start):
    k = 2
    while (((k*start)-offset) <= isprimelen-1):
        isprime[(k*start) - offset] = 0
        k += 1
    return isprime

def generate_prime_list(matrix_a, matrix_isprime):
    print "Started generate_prime_list."
    if len(matrix_a) != len(matrix_isprime):
        print "Matrix lengths are messed up."
        return
    matrix_result = []
    for i in range(isprimelen):
        if matrix_isprime[i] == 1:
            matrix_result.append(matrix_a[i])
    return matrix_result

def nextvalue(lastvalue):
    i = lastvalue - offset + 1
    while (i <= (end_value-offset)):
        if isprime[i] == 1:
            return (i + offset)
        else:
            i = i+1
    return (end_value+1)


end_value = 2*10**5
sievelist = range(2, end_value+1)
isprime = [1] * (end_value-1)
sievelistlen = len(sievelist)
isprimelen = len(isprime)
offset = sievelist[0]

postulatedprime = 2

while (postulatedprime <= end_value):
    isprime = sieve(postulatedprime)
    postulatedprime = nextvalue(postulatedprime)    
    
primes = generate_prime_list(sievelist, isprime)

if (len(primes) < 10001):
    print "Didn't use a long enough initial sieve list, no result."
    print "Length of primes is %d." % len(primes)
else:
    print "The 10,001st prime is %d." % primes[10000]
