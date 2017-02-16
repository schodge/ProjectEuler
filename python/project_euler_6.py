# Project Euler Problem 6
# 5/11/2012
# Copyright Shayne Hodge
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

sum = 0
delta = 0
for i in range(1,101):
    sum += i
print "The sum of 1 to 100 is %d, though your method is not as elegant as Gauss's." % sum

for i in range(1,101):
    delta += i*(sum-i)

print "The difference between the square of the sum and the sum of the squares is %d." % delta
    
