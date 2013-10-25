"""
Python3 Notes on Number Types

"""
## A Sample of Numeric Types

2**100
## 1267650600228229401496703205376

print("How many digits in 2**1000000?")
print(len(str(2**1000000)))

import math
print(math.pi)

import random
random.random()
random.choice([1,2,3,4])

## Numeric Literals and Constructors
## Literal followed by Interpretation

>>> 1234                        # Integers (unlimited size)
1234

>>> -24
-24

>>> 0
0

>>> 9999999999999999999999
9999999999999999999999

>>> 1.23                        # Floating-point numbers
1.23

>>> 1.
1.0

>>> 3.14e-10
3.14e-10

>>> 4E210
4e+210

>>> 4.0e+210
4e+210

'''
NOTE:  Integers can be coded in decimal (base 10), hexadecimal (base 16),
octal (base 8), or binary (base 2).
'''

>>> 0o177                       # Octal literal in 3.X
127

'''
NOTE: Octal literals start with a leading 0o or 0O (zero and lower- or uppercase
letter o), followed by a string of digits (0-7).
'''

>>> 0x9ff                       # Hex literal in 3.X
2559

>>> 0b101010                    # Binary literal in 3.X
42

'''
NOTE:  Binary literals are new as of 2.6 and 3.0.  They begin with a leading 0b
or 0B followed by binary digits (0-1).
'''

>>> 0177                       # Octal literal in 2.X
127

'''
In 2.X Octal literals can also be coded with just a leading 0, but not in 3.X.
'''

>>> 0o177
127

>>> 0x9ff                       # Hex literal in 2.X
2559

'''
NOTE:  Hex numbers start with a leading 0x or 0X followed by a string of
hexidecimal digits (0-9 and A-F).  They can be coded in lower case or
upper case.
'''

>>> 0b101010                    # Binary literal in 2.X
42

>>> 3 + 4j                      # Complex Number literal
(3+4j)

>>> 3.0 + 4.0j
(3+4j)

>>> 3J
3j

>>> complex(4,5)                # Use Complex Number constructor
(4+5j)

>>> set('spam')                 # Sets: 2.X and 3.X construction forms
{'m', 's', 'p', 'a'}

>>> {1, 2, 3, 4}
{1, 2, 3, 4}

>>> import decimal
>>> decimal.Decimal('1.0')      # Decimal literal
Decimal('1.0')

>>> from fractions import Fraction

>>> Fraction(1,3)               # Fraction extension type
Fraction(1, 3)

>>> bool(234)                   # Boolean type
True
>>> True                        # Boolean constants
True
>>> False
False

"""
NOTES:  If you write a number with a decimal point or exponent, Python makes
it a floating-point object and uses floating-point math when the object is used
in an expression.  Floating-point numbers are implemented as C "doubles" in
standard CPython, and therefore get as much precision as the C compiler
used to build the Python interpreter.

In Python 2.X there are two integer types, normal (often 32 bits) and long
(unlimited precision), and an integer may ed in an l or L to force it to
become a long (although Python will automatically convert to long if needed).

In Python 3.X there is only one integer type which supports unlimited precision.

"""

## Converting between various forms of integers
## Convert from decimal to hex, oct, or bin
>>> hex(234)
'0xea'

>>> oct(234)
'0o352'

>>> bin(234)
'0b11101010'

>>> int(234)
234

## Convert from hex to decimal
>>> int('0XEA',16)
234

## Convert from oct to decimal
>>> int('0o352', 8)
234

## Convert from bin to decimal
>>> int('0b11101010', 2)
234

## Python Expression Operators

"""
Operator                       Description
--------------------------------------------------------
yield x   .................... Generator function send protocol
lambda args: expression ...... Anonymous function generation
x if y else z ................ Ternary selection (x is evaluated only if y true
x or y ....................... Logical OR (y is evaluated only if x is false)
x and y ...................... Logical AND (y is evaluated only if x is true)
not x ........................ Logical negation 
x in y ....................... Membership (iterables, sets)
x not in y ................... Membership (iterables, sets)
x is y ....................... Object identity test
x is not y ................... Object identity test
x < y ........................ x is less than y, x subset of y

NOTE:  x < y < z is the same as x < y and y < z

x <= y ....................... x is less than or equal to y, x subset of y
x > y ........................ x is greater than y, x is superset of y
x >= y ....................... x is greater than or equal to y, x is superset of y
x == y ....................... x is equal to y (in value)
x != y ....................... x is not equal to y (in value)

x | y ........................ Bitwise OR, set union

x ^ y ........................ Bitwise XOR, set symmetric difference

x & y ........................ Bitwise AND, set intersection
x << y ....................... Shift x left by y bits
x >> y ....................... Shitf x right by y bits
x + y ........................ Addition of numbers, concatenation of strings
x - y ........................ Subtraction of numbers, set difference
x * y ........................ Multiplication, repetition
x % y ........................ Remainder, format of strings
x / y ........................ Division
x // y ....................... Integer Division (Division Floor)
-x ........................... Negation
+x ........................... Identity
~x ........................... Bitwise NOT (inversion)
x ** y ....................... Power (exponentiation)
x[i] ......................... Indexing (sequence, mapping, others)
x[i:j:k] ..................... Slicing

NOTE: you can also use x[slice(i,j,k)]

x(...) ....................... Call (function, method, class, other callable)
x.attr ....................... Attribute reference
(...) ........................ Tuple, expression, generator expression
[...] ........................ List, list comprehension
{...} ........................ Dictionary, set, set and dictionary comprehension
"""

### Operator Precedence
### In the table, Operators lower in the table have higher precedence, and
### so bind more tightly in mixed expressions
### Operators in the same row generally group from left to right when combined
### (except for exponentiation, which groups right to left, and comparisons,
### which chain left to right).

##The following table summarizes the operator precedences in Python, from
##lowest precedence (least binding) to highest precedence (most binding).
##Operators in the same box have the same precedence. Unless the syntax is
##explicitly given, operators are binary. Operators in the same box group
##left to right (except for comparisons, including tests, which all have
##the same precedence and chain from left to right — see section
##Comparisons — and exponentiation, which groups from right to left).

"""
Operator                       Description
--------------------------------------------------------
yield x   .................... Generator function send protocol
lambda args: expression ...... Anonymous function generation
x if y else z ................ Ternary selection (x is evaluated only if y true
x or y ....................... Logical OR (y is evaluated only if x is false)
x and y ...................... Logical AND (y is evaluated only if x is true)
not x ........................ Logical negation

in, not in, is, is not, <, <=, >, >=, <>, !=, ==


x | y ........................ Bitwise OR, set union

x ^ y ........................ Bitwise XOR, set symmetric difference

x & y ........................ Bitwise AND, set intersection
x << y, x >> y ............... Shitf x left or right by y bits
+, -
*, /, //, %
+, -, ~
x ** y ....................... Power (exponentiation)
x[i] ......................... Indexing (sequence, mapping, others)
x[i:j:k] ..................... Slicing

NOTE: you can also use x[slice(i,j,k)]

x(...) ....................... Call (function, method, class, other callable)
x.attr ....................... Attribute reference
(...) ........................ Tuple, expression, generator expression
[...] ........................ List, list comprehension
{...} ........................ Dictionary, set, set and dictionary comprehension


"""



