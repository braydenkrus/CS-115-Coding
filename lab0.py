############################################################
# Name: Brayden Krus
# Pledge: "I pledge my Honor that I have abided by the Stevens Honor System"
# CS115 Lab 1
############################################################

'''This function will say if the first and last letter of a word are the same.'''
def same(word):
    word = str.casefold(word)
    return word[0] == word[-1]

'''This function will find the sum of consecutive integers between two numbers.'''
def consecutiveSum(x, y):
    return ((x + y)/2) * (y - x - 1)