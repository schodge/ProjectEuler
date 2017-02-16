# Project Euler 9
# Copyright Shayne Hodge
# 5/11/2012
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

a = range (1, 333)

for i in a:
    b = i+1
    while (b <= 499):
        test = math.sqrt(i*i + b*b)
        if (test-int(test)) == 0:
            if (test + b + i) == 1000:
                print "a = %d b = %d c = %d a*a = %d b*b = %d c*c = %d" \
                      % (int(i), int(b), int(test), int(i*i), int(b*b), int(test*test))
                print "The product abc is %d." % int(i*b*test)
                break
        b += 1
