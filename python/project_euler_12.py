'''
Shayne Hodge
2/15/2014

Project Euler Problem 12

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Longest sequence under one million?
'''

#currently a brute force implementation with no niceities
# including, apparently, spell check in the comments
import numpy as np
import matplotlib.pyplot as plt

def make_hist(results):
    plt.hist(results, bins=100)

def next_number(n):
    next = n/2 if n%2 == 0 else (3*n+1)
    return next

def check_dict(results):
    pass
    # check if results in dictionary
    # return if true else return empty?

ending = 1000000
results = dict()
lengths = np.empty((ending-1,1))
for k in range(1, ending):
    temp = [k]
    n = k
    while n != 1:
        n = next_number(n)
        temp.append(n)
    results[k] =  temp
    lengths[k-1] = len(temp)

max_length = np.max(lengths)
max_length_idx = np.argmax(lengths)
print 'Max length is '+str(max_length)+' found at '+str(max_length_idx+1)+'.'
make_hist(lengths)