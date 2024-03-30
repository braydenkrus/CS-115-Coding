############################################################
# Name: Brayden Krus
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
############################################################

from math import factorial
from functools import reduce

'''The function inverse(x) will return the reciprocal of x, which is 1/x.'''
def inverse(x):
    return 1/x

'''The function adding(a,b) will add a and b together. Basically just referencing my recent lecture notes for this one.'''
def adding(a,b):
    return a + b

'''The function e(n) will approximate e by adding up the first n terms of 1/1! + 1/2! + 1/3! + . . ., and then adding 1 to that value to return the approximation'''
def e(n):
    list_num = list(range(1, n+1)) # gets numbers from 1 to user inputted number
    list_factorials = list(map(factorial,list_num)) # gets factorials of all numbers
    list_inverse = list(map(inverse, list_factorials))# takes reciprocals of factorial list 
    added = reduce(adding, list_inverse) #applies adding to all values in list_inverse
    added += 1 # we add 1 since the function starts at 1/1! and not 1.
    return added