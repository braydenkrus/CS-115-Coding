'''
Brayden Krus
"I pledge my honor that I have abided by the Stevens Honor System."
CS 115 Lab 2
'''

def list_length(n):
    '''takes the length of a list like the built-in len function would.
    I used the class notes from September 20th as reference.'''
    if n == []:
        return 0
    else:
        return 1 + list_length(n[1:])

def dot(L, K):
    '''dot(L, K) will output the dot product of the list L and the list K.'''
    if L == [] and K == []:
        return 0.0
    else:
        return (L[0] * K[0]) + dot(L[1:], K[1:])

def explode(S):
    '''this will break up a string into multiple 1 character strings'''
    if S == '':
        return []
    else:
        return [str(S[0])] + explode(S[1:])

def ind(e, L):
    ''' returns what index e appears at in L. if it doesnt appear,
    returns the length of L'''
    if L == [] or L == 0 or L == '':
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

def removeAll(e, L):
    ''' removes anything in the list that is equal to e'''
    if L == []:
        return []
    elif e == L[0]:
        return removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])

def myFilter(e, L):
    '''returns the elements (in L) the lambda (e) returns true for'''
    if L == []:
        return []
    elif e(L[0]) == True:
        return [L[0]] + myFilter(e,L[1:])
    else:
        return myFilter(e,L[1:])

def deepReverse(L):
    '''reverses the list, and every list element in the list if applicable'''
    if L == []:
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    else:
        return [L[-1]] + deepReverse(L[:-1])