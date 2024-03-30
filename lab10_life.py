#
# life.py - Game of Life lab
#
# Name: Brayden Krus
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    '''returns zeroes of width'''
    row = []
    for col in range(width):
        row += [0]
    return row
    
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    '''returns a width (col) * height (row) sized array'''
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

'''this is to import sys as stated'''
import sys

def printBoard(A):
    """ this function prints the 2d list-of-lists
A without spaces (using sys.stdout.write)
    """
    '''this prints out the array'''
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

A = createBoard(5,3)
printBoard(A)

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    '''this prints a diagonal strip of cells that are on'''
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

A = diagonalize(7,6)
print(A)
printBoard(A)

def innerCells(w,h):
    '''this sets the inner cells equal to 1, with the outer cells
    (border) being only 0'''
    A = createBoard(w,h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = 1
    return A

printBoard(innerCells(5,5))

def randomCells(w,h):
    '''this will make an array with 0 as the outer border,
    and a random arrangement of 0s and 1s on the inside of it
    '''
    A = createBoard(w,h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = random.choice([0,1])
    return A

printBoard(randomCells(10,10))

def copy(A):
    '''this will create a deep copy of our original array A.'''
    newA = createBoard(len(A[0]),len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            newA[row][col] = A[row][col]
    return newA

oldA = createBoard(2,2)
printBoard(oldA)
newA = copy(oldA)
printBoard(newA)
oldA[0][0] = 1
printBoard(oldA)
printBoard(newA)

def innerReverse(A):
    '''this will leave the border of an array as 0s.
    everything inside is flipped, so every 0 becomes
    a 1, and every 1 becomes a 0.'''
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if A[row][col] == 0:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

A = randomCells(8,8)
printBoard(A)
A2 = innerReverse(A)
printBoard(A2)

def next_life_generation(A):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    '''this will perform Conway's game of line within the inner cells'''
    newA = copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            neighbors = countNeighbors(row,col,A)
            if A[row][col] == 1 and (neighbors > 3 or neighbors < 2):
                newA[row][col] = 0
            elif A[row][col] == 0 and neighbors == 3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]
    return newA

def countNeighbors(row,col,A):
    '''this will count the amount of (alive) neighbors
    around each inner cell. this is made according to the
    visual in the comment below:
    '''
    # (1,1) (1,2) (1,3)
    # (2,1) (2,2) (2,3)         (2,2) is the cell we are working with
    # (3,1) (3,2) (3,3)
    one = A[row-1][col-1]
    two = A[row-1][col]
    three = A[row-1][col+1]
    four = A[row][col-1]
    five = A[row][col+1]
    six = A[row+1][col-1]
    seven = A[row+1][col]
    eight = A[row+1][col+1]
    return (one + two + three + four + five + six + seven + eight)

A = [ [0,0,0,0,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,0,0,0]]
printBoard(A)
A2 = next_life_generation(A)
printBoard(A2)
A3 = next_life_generation(A2)
printBoard(A3)