'''
Created on October 7th, 2023
@author:   Brayden Krus
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    '''this will give the minimum amount of coins to make an amount
    and also a list of what was used to make that amount.'''
    if amount == 0: #(0, [50]), (50, [])
        return [0, []]
    elif len(coins) == 0: # (20, [])
        return [float("inf"), []]
    elif coins[0] > coins[-1]:
        return giveChange(amount, coins[::-1])
    elif coins[-1] > amount:
        return giveChange(amount, coins[:-1])
    else:
        use_it = giveChange(amount - coins[-1], coins)
        use_it = [1 + use_it[0], [coins[-1]] + use_it[1]] # this increases the effeciency of the code instead of redefining use_it in one line
        lose_it = giveChange(amount, coins[:-1])
        if lose_it[0] > use_it[0]:
            return use_it
        else:
            return lose_it

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''

    '''This function will return the words with their scores'''
    def wordScore(word, scores):
        '''this function goes word by word'''
        if word == '':
            return 0
        else:
            return letterScore(word[0], scores) + wordScore(word[1:], scores)
    def wordScoreHelper(word): 
        '''this is crucial as map wouldn't work for scores, as it would use the terms from map once and then never again'''
        return [word, wordScore(word, scores)]
    def letterScore(letter, scores):
        '''this function goes letter by letter and scores them'''
        if letter == scores[0][0]:
            return scores[0][1]
        else:
            return letterScore(letter, scores[1:])
    return list(map(wordScoreHelper, dct))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    '''This function will return the first n values of a list.'''
    if n >= len(L):
        return L
    elif n == 0:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    '''This function will get rid of the first n values in a list.'''
    if n >= len(L):
        return []
    elif n == 0:
        return L
    else:
        return drop(n-1, L[1:])