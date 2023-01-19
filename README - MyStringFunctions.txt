PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

In this assignment, you'll be defining a collection of functions on strings, most of which already exist as methods on the str class. However, you should pretend that they don't already exist and define them as functions. Of course, you can't just use the existing methods. This will give you a bunch of practice on manipulating strings and also on defining functions.

In this assignment, you'll be defining a collection of functions on strings. You should define each of these as a new function with function header as below. The description of each is in the comment supplied. Recall that strings are immutable, so you will have to return a new copy of the string for those that want you to return a string. If you are returning the same string as the input, just return it; there is no need to make a new copy, and it wouldn't anyway.

The only string functions/methods you can use in this assignment are:

1. ord, chr
2. indexing and slicing
3. append (i.e., ``+'')
4. len, in, not in
5. equality comparison (== or !=))

Of course you can use other Python programming constructs such as looping over strings (while or for loops) and selection (if statements). Do not convert the strings to other types such as lists.

Define each of the following functions, with semantics as indicated by the comment. In each of the following ch is a single character, s, s1, s2 are strings, and i is a non-negative integer. You do not have to validate the inputs, except as indicated; you can assume these types.

At least one question asks you to return two values. That really means returning a tuple (pair) of values. You do that as follows:

   return value1, value2

This actually returns the pair (value1, value2). The caller can then assign the members of the pair to two variables:

   x, y = pairReturningFunction()     # assumes function returns a pair
   z, w = (value1, value2)            # assigning a tuple to 2 variables

If you like, you can use earlier functions in later ones, or define helper functions, though it shouldn't really be necessary. Note that some of these are trivial to write, while others are a bit harder. I have done the first one for you.

def myAppend( s, ch ):
    # Return a new string that is like s but with 
    # character ch added at the end
    return s + ch

def myCount( s, ch ):
    # Return the number of times character ch appears
    # in s.

def myExtend( s1, s2 ):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.

def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.

def myPop( s, i ):
    # Return two results: 
    # 1. a new string that is like s but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(s), and return s unchanged and None

def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.

def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.

def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.

def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.

def myReverse( s ):
    # Return a new string like s but with the characters
    # in the reverse order. 

Expected output:

Below is the output from the functions I wrote for this assignment:

>>> from MyStringFunctions import *
>>> s1 = "abcd" 
>>> s2 = "efgh"
>>> myAppend( s1, "e" )
'abcde'
>>> myCount( s1, "e")
0
>>> myCount( s1, "a")
1
>>> myCount( "abcabc", "a")
2
>>> myExtend( s1, s2 )
'abcdefgh'
>>> myMin( "" )
Empty string: no min value    # Note the None doesn't print
>>> myMin( "zqralm" )
'a'
>>> myMin( "Hello World!" )
' '
>>> myInsert( "abc", 0, "d")
'dabc'
>>> myInsert( "abc", 2, "d")
'abdc'
>>> myInsert( "abc", 4, "d")     
Invalid index                 # Note the None doesn't print
>>> myPop( "abcd", 1 )
('acd', 'b')
>>> myPop( "abcd", 0 )
('bcd', 'a')
>>> myPop( "abcd", 5)
Invalid index
('abcd', None)
>>> myFind( "abcdabcd", "a")
0
>>> myFind( "abcdabcd", "c")
2
>>> myFind( "abcdabcd", "f")
-1
>>> myRFind("abcdabcd", "d")
7
>>> myRFind("abcdabcd", "e")
-1
>>> myRemove( "abcdabcd", "a")
'bcdabcd'
>>> myRemove( "abcdabcd", "x")
'abcdabcd'
>>> myRemove( "abcdabcd", "d")
'abcabcd'
>>> myRemoveAll("abcabcabca", "a")
'bcbcbc'
>>> myReverse( "abcd" )
'dcba'
>>> myReverse( "" )
''

