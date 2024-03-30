'''
Created on October 18, 2023
@author:   Brayden Krus
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    '''Will determine if an integer is odd.'''
    if n % 2 == 1:
        return True
    else:
        return False
# base-2 representation of 42: 101010

# if given an odd base-10 number, the rightmost base-2 digit will be 1 (as 2^0 = 1, the only odd base 2 number)
# if given an even base-10 number, the rightmost base-2 digit will be 0 (as 2^0 = 1, the only odd base 2 number)

# 1010 -> 101 is the same as 10 -> 5, dividing by 2.
# 1011 -> 101 is the same as 11 -> 5, dividing by 2.2.

# for y = N/2, to find the base representation of N, we would add a 1 at the end if the base-10 number is odd, and a 0 if the base-10 number is even


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    '''this will return a string of the binary version of an integer. goes right to left'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + '1'
    else:
        return numToBinary(n // 2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    '''this sets up a helper function that will return the binary string in base-10 form'''
    return btn_helper(s, 1)

def btn_helper(s, a = 1):
    '''this will return an integer of the base-10 version of a binary number. goes right to left'''
    if s == '':
        return 0
    elif isOdd(int(s[-1])):
        return btn_helper(s[:-1], a * 2) + (1 * a) # needs to be like ...16 8 4 2 1 so the value can go up      
    else:
        return btn_helper(s[:-1], a * 2)


def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    '''this will return an 8 bit binary value + 1'''
    if s == '11111111':
        return '00000000'
    x = numToBinary(binaryToNum(s) + 1)
    if len(x) != 8:
        y = (8 - len(x)) * '0'
        x = y + x
    return x

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    '''this will print a list of strings including start and end while counting up by an increment n'''
    print(s) # i have no idea why this makes it work, but it does for some reason
    if n == 0:
        return s
    else:
        return s + count(increment(s), n - 1)
    
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    '''this will represent n in ternary form'''
    if n == 0:
        return ''
    elif n % 3 == 2:
        return numToTernary(n // 3) + '2'
    elif n % 3 == 1:
        return numToTernary(n // 3) + '1'
    else:
        return numToTernary(n // 3) + '0'
    
'''print(numToTernary(10)) # '101'
#10 % 3 = 1. 10 // 3 = 3
3 % 3 = 0. '''

# 59 would be 2012. 2*27 = 54, 1*3 = 3, 2*1 = 2. add them and you get 59
# 59 % 3 = 2. 59 // 3 = 19
# 19 % 3 = 1. 19 // 3 = 6
# 6 % 3 = 0.  6 // 3 = 2
# return that value    ^


def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    '''this sets up a helper function that will return the ternary string in base-10 form'''
    return ttn_helper(s, 1)

def ttn_helper(s, a = 1):
    '''this will return an integer of the base-10 version of a ternary number. goes right to left'''
    if s == '':
        return 0
    elif int(s[-1]) % 3 == 2:
        return ttn_helper(s[:-1], a * 3) + (2 * a)
    elif int(s[-1]) % 3 == 1:
        return ttn_helper(s[:-1], a * 3) + (1 * a)
    else:
        return ttn_helper(s[:-1], a * 3)