# Project Euler Problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 5/11/2012
# Copyright Shayne Hodge

i = 2520
eureka = False

while not(eureka):
    if (((i%11)==0) and ((i%12)==0) and ((i%13)==0) and ((i%14)==0) and ((i%15)==0) and \
       ((i%16)==0) and ((i%17)==0) and ((i%18)==0) and ((i%19)==0) and ((i%20)==0)):
        eureka = True
    else:
        i += 20

print i
