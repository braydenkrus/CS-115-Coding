'''
Created on October 29, 2023
@author:   Brayden Krus (did it on my own by choice)
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''
    This is a (somewhat) modified code from my Lab 6 submission that just converts base-10 numbers to binary numbers.
    '''
    if n == 0:
        return ''
    elif n % 2 == 1:
        return numToBinary(n // 2) + '1'
    else:
        return numToBinary(n // 2) + '0'

def bit_length(n):
    '''
    This is a (somewhat) modifed code from my Lab 6 submission that makes the length of every X1, X2, . . . , XN 
    sequence equal to COMPRESSED_BLOCK_SIZE
    '''
    if len(n) != COMPRESSED_BLOCK_SIZE:
        return (COMPRESSED_BLOCK_SIZE - len(n)) * '0' + n
    else:
        return n

def bit_to_num(s, a = 1):
    '''
    This is a (somewhat) modified code from my Lab 6 submission that converts binary numbers to base 10 numbers.
    '''
    if s == '':
        return 0
    elif int(s[-1]) % 2 == 1:
        return bit_to_num(s[:-1], a * 2) + (1 * a)
    else:
        return bit_to_num(s[:-1], a * 2)

def counting(S, MAX, count, NOT):
    '''
    This counts the number of 0s or 1s until the next 0 or 1 which can go on a range from 0-MAX_RUN_LENGTH.
    If S[0] == NOT, that means it was equal to the value we need to end at. 
    '''
    if len(S) == 0 or MAX <= 0:
        return count
    elif S[0] == NOT:
        return count
    else:
        return counting(S[1:], MAX-1, count+1, NOT)
    
def list_to_str(l):
    '''
    This just converts lists to strings.  
    '''
    if len(l) == 0:
        return ''
    else:
        return str(l[0]) + list_to_str(l[1:])

def compress(S):
    '''
    Through various helper functions, this function compresses a series of bits into a run-length sequence in bits. 
    It returns the list of decimal nums, then returns the list of binary nums, then makes the binary nums the same 
    length as each other (COMPRESSED_BLOCK_SIZE), and then returns the list as a string.
    '''
    return list_to_str(list(map(lambda b:bit_length(b), list(map(lambda a:numToBinary(a), compress_helper(S,MAX_RUN_LENGTH, [], 1))))))

# 1st comment
# Your compress function may sometimes give output that is actually longer than its input. In a
# comment, explain what is the largest number of bits that your compress algorithm could
# possibly use to encode a 64-bit string/image.
#
#
# The largest number of bits the compress algorithm would need to encode
# a 64-bit string/image is 64 * COMPRESSED_BLOCK_SIZE. So in the case of this
# assignment, that would be 64 * 5, which is 320. This would assume each bit is different from the last,
# so 1010...1010 or 0101...0101 would be examples where this would come up.

def compress_helper(S, MAX, numlist, eo):
    '''
    This function returns a list of decimal numbers representing the run-length sequence. eo is used for
    "XODD" and "XEVEN", as "XODD" (X1, X3, . . .) counts how many 0s  there arebefore a 1, and 
    "XEVEN" (X2, X4, . . . ) counts how many 1s there are before a 0.
    '''
    if len(S) == 0:
        return numlist
    elif S[0] == '0' and eo % 2 == 1:
        x = counting(S, MAX, 0, '1')
        numlist.append(x)
        return compress_helper(S[x:], MAX, numlist, eo + 1)
    elif S[0] == '1' and eo % 2 == 0:
        x = counting(S, MAX, 0, '0')
        numlist.append(x)
        return compress_helper(S[x:], MAX, numlist, eo + 1)
    else:
        numlist.append(0)
        return compress_helper(S, MAX, numlist, eo + 1)

# this is just me figuring out test 1.
# '1111100000111110000000010'
# 64 zeros.
# X1, X2, ... , X(N-1), X(N) are all (COMPRESSED_BLOCK_SIZE) long 
# X(ODD) represents how many 0s come before the next 1.
# X(EVEN) represents how many 1s come before the next 0.
# breaking down 64 zeros -> '1111100000111110000000010'
# '|11111|00000|11111|00000|00010'
#   X1     X2    X3     X4    X5
# X1: 16 + 8 + 4 + 2 + 1 = 31 0s before the next 1.
# X2: 0 + 0 + 0 + 0 + 0 = 0 1s before the next 0.
# X3: 16 + 8 + 4 + 2 + 1 = 31 0s before the next 1.
# X4: 0 + 0 + 0 + 0 + 0 = 0 1s before the next 0.
# X5: 0 + 0 + 0 + 2 + 0 = 2 0s before the next 1.

def uncompress(S): # X1 binary to decimal, add that many 0s, X2 binary to decimal, add that many 1s, . . .
    '''
    With the help of uncompress_helper, this function uincompresses our run-length sequence of binary numbers into one big binary sequence. 
    '''
    return uncompress_helper(S,1)

def uncompress_helper(S, eo):
    '''
    This function will use the amounts stored in XODDs and XEVENs to count the correct amount of 0s and 1s
    '''
    if len(S) == 0:
        return ''
    elif eo % 2 == 1: # XODD, COUNTING '0'
        return ('0' * bit_to_num(S[:COMPRESSED_BLOCK_SIZE])) + uncompress_helper(S[COMPRESSED_BLOCK_SIZE:], eo + 1)
    elif eo % 2 == 0: # XEVEN, COUNTING '1'
        return ('1' * bit_to_num(S[:COMPRESSED_BLOCK_SIZE])) + uncompress_helper(S[COMPRESSED_BLOCK_SIZE:], eo + 1)

def compression(S):
    '''
    This simply divides the length of our compressed sequence by the length of the original sequence.   
    '''
    return len(compress(S)) / len(S)

Penguin = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
Smile =  "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
Five = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"

print(compression(Penguin))
print(compression(Smile))
print(compression(Five))

# 2nd comment
# Test your compression algorithm on several test images of your own design. In a
#comment, describe the tests that you conducted and the compression ratios that you found. You
#may find it useful to write some additional functions to help automate the testing of
#your compress algorithm. Here are a few test "images" that we are providing:
#
#
# I just used the given text examples to do this. It turns out that all of the
# cases here are actually bigger in size than they were. Although for some of the test cases
# on the actual test document, some of the compressed sizes were smaller. All of this is to say
# that the efficiency of our compression varies.

# 3rd comment
# Professor I. Lai from the Pasadena Institute of Technology (P.I.T.) has made the following claim
# to NASA: "I have developed a new image compression algorithm Laicompress(S) that takes a
# 64-bit string and always outputs a shorter string that represents that image. That is, every image
# is compressed at least somewhat by my algorithm. Of course, I also have Laiuncompressthat
# inverts the Laicompress algorithm so that Laiuncompress(Laicompress(S)) gives
# back S. In a comment, argue to NASA that Professor Lai is Lai-ing—such an algorithm cannot
# exist! Try to make your reasoning as convincing and water-tight as possible. (In essence, you are
# proving that such an algorithm cannot exist.
#
#
# This function cannot exist because given this structure of compression,
# there will always be cases in which the string is longer than the original code.
# For example, if a string was basic ex: '10' * 32, it would need to account for
# each bit switch, which takes 5 bits per 1 bit in the original string.
# I'll also mention my knowledge from AP Computer Science Principles, and if 
# a sequence of letters/numbers/spaces/symbols/etc. never shows up more than once in
# a string, then it is already as compressed as can be.
# In short, unless our compression is constructed differently, it won't always be efficient.