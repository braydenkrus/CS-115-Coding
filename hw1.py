# Brayden Krus
# I pledge my honor that I have abided by the Stevens Honor System.

'''importing the reduce function for factorial(n)'''
from functools import reduce

'''this will take the factorial of n (n!).'''
def factorial(n):
     return(reduce(lambda x,y: x * y, list(range(1,n+1))))

'''this will take the mean (average) of the numbers in a list.'''
def mean(L):
    return((reduce(lambda a,b: a + b, L)) / (len(L)))