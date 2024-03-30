'''
Created on September 27th, 2023
Rewritten on March 23rd, 2024 and March 24th, 2024
@author:   Brayden Krus
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
  '''returns the appropriate score of a letter based on the provided scorelist'''
  if letter == scorelist[0][0]:
      return scorelist[0][1]
  else:
      return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
  '''returns the appropriate score of a word based on the provided scorelist'''
  if S == "" or S == '' or scorelist == []:
    return 0
  elif S[0] != scorelist[0][0]:
    scorelist.append(scorelist[0])
    return wordScore(S, scorelist[1:])
  else:
    return scorelist[0][1] + wordScore(S[1:], scorelist)
  
def StoList(S):
   '''converts a string into a list of 1 character strings'''
   if S == '' or "":
      return []
   else:
      return [S[0]] + StoList(S[1:])
  
def rackCompare(Rack, S, TF):
   '''this lets us check the common letters between a rack and a word'''
   if (S == []) and (False in TF):
      return False
   if (S == []):
      return True
   if S[0] in Rack:
      i = Rack.index(S[0])
      S.remove(S[0])
      Rack[i] = "used"
      TF.append(True)
      return rackCompare(Rack, S, TF)
   else:
      return False

def recursiveCompare(Rack,a):
   '''helper for rackCompare'''
   if a == []:
      return []
   else:
      newRack = Rack[:]
      return [rackCompare(newRack, a[0], [])] + recursiveCompare(Rack, a[1:])
   
def removeFalse(b, d, new):
   '''helper for scoreList to only add the words with letters from the rack'''
   if b == [] or d == []:
      return new
   if b[0] == True:
      new.append(d[0])
      return removeFalse(b[1:], d[1:], new)
   if b[0] == False:
      return removeFalse(b[1:], d[1:], new)
   
def scoreListBuilder(c,d):
   '''helper for scoreList to assign each word to its proper score'''
   if c == [] or d == []:
      return []
   else:
      return [[c[0], d[0]]] + scoreListBuilder(c[1:],d[1:])

def scoreList(Rack):
   '''returns the list of words that can be made from the rack'''
   a = list(map(lambda S: StoList(S), Dictionary))
   b = recursiveCompare(Rack, a)
   c = removeFalse(b, Dictionary, [])
   d = list(map(lambda S: wordScore(S, scrabbleScores), c))
   e = scoreListBuilder(c,d)
   return e

def bestHelper1(a, max):
   '''helper for bestWord to find the highest scoring word'''
   if a == []:
      return max
   if a[0][1] > max:
      return bestHelper1(a[1:], a[0][1])
   else:
      return bestHelper1(a[1:], max)
   
def bestHelper2(b, c):
   '''helper for bestWord to return the highest scoring word'''
   if b[0][1] == c:
      return b[0]
   else:
      return bestHelper2(b[1:], c)

def bestWord(Rack):
   '''returns the highest scoring word that can be made from the rack'''
   a = scoreList(Rack)
   if a == []:
      return ['', 0]
   b = scoreList(Rack)
   max = 0
   c = bestHelper1(a,max)
   d = bestHelper2(b,c)
   return d