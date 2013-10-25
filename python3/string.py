"""
Python3 Notes on Strings

"""
## String Literals
print('She said, "What\'s your name?"')
print("""Here is a string
accross multiple lines
what do you think?""")
print("Here's an example of a raw string:")
# raw turns off the backslash escape mechanism
s = r'C:\Program Files\Office'
print(s)

S = 'Spam'
print("S = '" + str(S) + "'        # Make a 4-character string, assign it to S")
print('len(S) = ', len(S), "      # Length")
print("S[0] = '" + S[0] + "'        # The first item in S, indexing by zero")
print("S[1] = '" + S[1] + "'        # The second item from the left")
print("S[-1] = '" + S[-1] + "'       # The last item from the end in S")
print("S[-2] = '" + S[-2] + "'       # The second-to-last item from the end")
print("S[len(S)-1] = '" + S[len(S)-1] + "' # Negative indexing the hard way")
print("S[1:3] = '" + S[1:3] + "'     # Slice of S offsets 1 through 2 (not 3)")
print("S[1:] = '" + S[1:] + "'     # Everything past the first (1:len(S))")
print("\nAfter all of this S hasn't changed!\n")
print("S = '" + S + "'        # Strings are immutable!")
print("S[0:3] = '" + S[0:3] + "'    # Everything but the last")
print("S[:3] = '" + S[:3] + "'     # Everything but the last")
print("S[:-1] = '" + S[:-1] + "'    # Everything but the last")
print("S[:] = '" + S[:] + "'     # All of S as a top-level copy (0:len(S))")
print("\nOperations on Strings\n")
print("S + 'xyz' = '" + (S + 'xyz') + "'    # Concatenation, Example of Polymorphism")
print("                         # + is overloaded:  Concatenation for Strings")
print("                         # addition for numbers")
print("S = '" + S + "'               # Strings are immutable!")
print("S * 3 = '" + (S * 3) + "'   # Repetition")
print("S[0] = 'z'               # Causes Exception: TypeError: ")
print("                         #'str' object does not support item assignment")
print("\nS = 'z' + S[1:] returns '" + ('z'+S[1:]) + "' for S\n") 
S = 'shrubbery'
print("S = '" + str(S) + "'          # assign S to a new string")
L = list(S)
print("L = list(S)              # Exapand S to a list")
print("\nL = " + str(L) + "\n")
print("L[1] = 'c'               # List are mutable, so change it in place")
L[1] = 'c'
print("\nNow L = " + str(L) + "\n")
print("''.join(L)               # Join with the empty delimeter gives")
print("'" + ''.join(L) + "'")
print("\nYou can use bytearray for in-place changes for text, but only for ")
print("text whose characters are all at most 8-bits wide (e.g. ASCII)\n")
B = bytearray(b'spam')
print("B = bytearray(b'spam')   # A bytes/list hybrid?")
B.extend(b'eggs')
print("B.extend(b'eggs')        # 'b' needed in 3.X, not 2.X")
print("B is now:")
print(B)
print("B.decode()               # Translate return a normal string")
print("'" + str(B.decode()) + "'")
print("B is still:")
print(B)
print("more information on bytearrays:")
print("http://dabeaz.blogspot.com/2010/01/few-useful-bytearray-tricks.html")
print("\nNote:  All the operations above work on any 'sequence'.  This means")
print("for example, that they will also work on Lists and Tuples.")
print("\nString-Specific Methods:\n")
print("""
>>> S = 'Spam'
>>> S.find('pa')               # Find the offset of a substring in S
1
>>> S.find('B')                # return -1 if substring not found
-1
>>> S
'Spam'
>>> S.replace('pa', 'XYZ')     # Replace occurrences of a string in S with another
'SXYZm'
>>> S                          # Don't forget that strings are immutable
'Spam'
>>> S.replace('B', 'C')
'Spam'
>>> line = 'aaa,bbb,ccccc,dd'  # Split on a delimiter into a list of substrings
>>> line.split(',')
['aaa', 'bbb', 'ccccc', 'dd']
>>> S = 'spam'
>>> S.upper()                  # Convert to upper case
'SPAM'
>>> S.isalpha()                # return True if all char are alphabetic (and nonempty)
True
>>> S.lower()                  # Convert to lower case
'spam'
>>> 'Hello WORLd'.lower()
'hello world'
>>> '5'.isdigit()              # return True if all char are digits (and nonempty)
True
>>> '5a'.isdigit()
False
>>> line = 'aaa,bbb,ccccc,dd\n'
>>> line.rstrip()              # Remove whitespace characters on the right side
'aaa,bbb,ccccc,dd'
>>> line.rstrip().split(',')   # Combine two operations
['aaa', 'bbb', 'ccccc', 'dd']
>>> '%s, eggs, and %s' % ('spam', 'SPAM!')  # Formatting expression (all)
'spam, eggs, and SPAM!'
>>> '{0}, eggs, and {1}'.format('spam', 'SPAM!') # Formatting method (2.6+, 3.0+)
'spam, eggs, and SPAM!'
>>> '{}, eggs, and {}'.format('spam', 'SPAM!')  # Numbers optional (2.7+, 3.1+)
'spam, eggs, and SPAM!'
>>> '{:,.2f}'.format(296999.2567)     # Sepators, decimal digits
'296,999.26'
>>> '%.2f | %+05d' % (3.14159, -42)   # Digits, padding, signs
'3.14 | -0042' 
""")
      
## Unicode
"""
>>> 'sp\xc4m'    # 3.X: normal str string are Unicode text
'spÄm'
>>> b'a\x01c'    # bytes strings are byte-based data
b'a\x01c'
>>> u'sp\u00c4m' # The 2.X Unicode literal works in 3.3+: just str
'spÄm'
"""

## Formally, in both 2.X and 3.X, non-Unicode strings are sequences of 8-bit
## bytes that print with ASCII characters when possible, and Unicode strings
## are sequences of Unicode code points -- identifying numbers for characters,
## which do not necessarily map to single bytes when encoded to files or
## stored in memory.  Here are some examples:
"""
>>> 'spam'                   # Characters may be 1, 2, or 4 bytes in memory
'spam'
>>> 'spam'.encode('utf8')    # Encoded to 4 bytes in UTF-8 in files
b'spam'
>>> 'spam'.encode('utf16')   # Now encoded to 10 bytes in UTF-16
b'\xff\xfes\x00p\x00a\x00m\x00'
"""
## Both 3.X and 2.X also support coding non-ASCII characters with \x hexadecimal
## and short \u and long \U Unicode escapes.  Here's our non-ASCII character
## coded three ways in 3.X
"""
>>> 'sp\xc4\u00c4\U000000c4m'
'spÄÄÄm'

"""
