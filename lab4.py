# Brayden Krus
# I pledge my honor that I have abided by the Stevens Honor System.

def knapsack(capacity,itemList):
    '''This code will determine the best items to take based on how much you can carry, and how much each item is worth.
    I used the code from the Knapsack Problem.pdf presentation in class as a start, which was very helpful.'''
    if len(itemList) == 0 or capacity <= 0: # base case
        return [0, []]
    elif itemList[0][0] > capacity: # get rid of it if its too big
        return knapsack(capacity, itemList[1:])
    else:
        use_it = [itemList[0][1] + knapsack(capacity - itemList[0][0], itemList[1:])[0], [itemList[0]] + knapsack(capacity - itemList[0][0], itemList[1:])[1]]
        '''the above use_it code will give a list that is [value, [list of items used]]
        knapsack(...)[0] is an integer, knapsack(...)[1] is a list.'''
        lose_it = knapsack(capacity, itemList[1:])
        '''for the code below, we effectively do max of use_it[0] and lose_it[0] and then return
        the highest list basically'''
        if use_it[0] > lose_it[0]:
            return use_it
        else:
            return lose_it