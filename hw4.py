# Brayden Krus
# I pledge my honor that I have abided by the Stevens Honor System.

def pr_helper(R, Rnext = []): 
    '''this function will create a new list of sums stored by adjacent terms (so like for [1, 3, 3, 1], 1+3=4, 3+3=6, and 3+1=4 get put in,
    so it would be [4, 6, 4]. it then puts 1 at the beginning and the end to return [1, 4, 6, 4, 1])'''
    if len(R) == 1:
        Rnext.insert(0, 1)
        Rnext.append(1)
        return Rnext
    else:
        x = R[0] + R[1]
        Rnext.append(x)
        return pr_helper(R[1:], Rnext)

def pascal_row(n, R = [1]):
    '''this function will return row n of Pascal's Triangle, with the help of the above helper function'''
    if n == 0:
        return R
    elif R == [1]:
        return pascal_row(n-1, [1,1])
    else:
        return pascal_row(n-1, pr_helper(R, []))

def pt_helper(n, R = [1], R_list = [[1]]):
    '''this function will return a list of every row of Pascal's Triangle from 0 to n'''
    if n == 0:
        return R_list
    elif R == [1]:
        R_list.append([1,1])
        return pt_helper(n-1, [1,1], R_list)
    else:
        x = pr_helper(R, [])
        R_list.append(x)
        return pt_helper(n-1, x, R_list)
    
def pascal_triangle(n):
    '''this function will, in the end, return a list of every row of Pascal's Triangle from 0 to n. the only thing happening here is that
    it will call the pt_helper function to make sure the R and R_list values reset each time.'''
    return pt_helper(n, [1], [[1]])

def test_pascal_row():
    '''this function will test the pascal_row function with some calls'''
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]
    assert pascal_row(6) == [1, 6, 15, 20, 15, 6, 1]
    assert pascal_row(8) == [1, 8, 28, 56, 70, 56, 28, 8, 1]

def test_pascal_triangle():
    '''this function will test the pascal_triangle function with some calls'''
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(8) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1]]
