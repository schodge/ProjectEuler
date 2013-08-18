#Project Euler Problem 4
#May 10, 2012
#Copyright Shayne Hodge
#Find the largest palindrome made from the product of two 3-digit numbers.

def ispalindrome(testnum):
    number = str(testnum)
    ispalin = False
    if len(number) == 5:
        if (number[0] == number[4]) and (number[1] == number[3]):
            ispalin = True
    elif len(number) == 6:
          if (number[0] == number[5]) and (number[1] == number[4]) and (number[2] == number[3]):
            ispalin = True
    else:
        print "Number not within expected bounds"
    return ispalin


a = b = 999

print a
print b

hold_a = hold_b = hold_palin = 0
while (a>99):
    while (b>99):
        test = ispalindrome(a*b)
        if test and ((a*b) > hold_palin):
            hold_a = a
            hold_b = b
            hold_palin = a*b
        b -= 1
    a -= 1
    b = a
    if (a*b) < hold_palin:
        print "Breaking at a = %d and b = %d" % (a, b)
        break

programout = 'a = ' + str(hold_a) + ' b = ' + str(hold_b) + ' giving a*b = ' + str(hold_palin) +'.'
print programout
