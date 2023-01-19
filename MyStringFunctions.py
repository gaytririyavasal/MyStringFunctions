# File: MyStringFunctions.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 10/22/2021
# Date Last Modified: 10/25/2021
# Description of Program: The following program defines a collection of functions on strings.

def myAppend( str, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count = 0

    for chr in str:
        if(chr == ch):
            count += 1

    return count

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.

    return str1 + str2

def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.

    if (str == ""):
        print("Empty string: no min value")
        return None
    else:
        c = 0
        for i in range(len(str)):
            ch = str[i]
            if (c == 0):
                min = ch
                c += 1
            else:
                if(ord(ch) < ord(min)):
                    min = ch

        return min

def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.

    if(i > len(str)):
       print("Invalid index")
       return None
    else:
        sone = str[0 : i]
        stwo = str[i : ]
        return sone + ch + stwo
    
def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    
    if(i >= len(str)):
        print("Invalid index")
        return str, None

    else:
        sone = str[0 : i]
        stwo = str[i+1 : ]
        ch = str[i]
        return sone + stwo, ch

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.

    for i in range(len(str)):
        character = str[i]
        if(character == ch):
            return i
    return -1

def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.

    for i in range(len(str)):
        character = str[-i]
        if(character == ch):
            return -i+len(str)
    return -1

def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.

    for i in range(len(str)):
        character = str[i]
        if(character == ch):
            return str[0 : i] + str[i+1 : ]
    return str
    
def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.

    string = ""
    
    for i in range(len(str)):
        character = str[i]
        if(character != ch):
            string += character

    return string

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.

    string = ""
    
    for i in range(1, len(str)):
        character = str[-i]
        string += character

    if(string != ""):
        string += str[0]

    return string

