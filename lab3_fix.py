# Brayden Krus
# I pledge my honor that I have abided by the Stevens Honor System.

def change(amount, coins): 
    '''This code will return the lowest number of coins we need to get to an amount. '''
    if amount > 0 and coins == []: # base case 1 
        '''on the doc it said if theres no coins to make amount, it returns inf'''
        return float("inf")
    elif amount <=0 or coins == []: # base case 2
        '''this base case is good for when we are done, as if there are coins, coins[0] is always 1,
        and from the recursion we've done I know that 0, '', or [] are almost always the base case'''
        return 0
    elif coins[-1] > amount: 
        '''gets rid of coins that are too high at the start, and as we progress through the cases'''
        return change(amount, coins[:-1])
    else:
        use_it = 1 + change(amount - coins[-1], coins) # subtract current highest coin from amount, recall with the coin
        lose_it = change(amount, coins[:-1]) # lose the coin even though it could have be used
        return min(use_it, lose_it)