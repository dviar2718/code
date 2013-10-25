"""
Python3 notes on tuples

A tuple is roughly like a list that cannot be changed.  Tuples are sequences
like lists but they are immutable like strings.

Typical uses: represent fixed collections of items such as the components
of a specific calendar date.

"""

>>> T = (1, 2, 3, 4)                 # A 4-item tuple

>>> len(T)                           # Length
4

>>> T + (5, 6)                       # Concatenation
(1, 2, 3, 4, 5, 6)

>>> T[0]                             # Indexing, slicing, and more
1

## Tuples also have type-specific callable methods as of Python 2.6 and 3.0
## but not nearly as many as lists:

>>> T.index(4)                       # Tuple methods:  4 appears at offset 3
3

>>> T.count(4)                       # 4 appears once
1

>>> T[0] = 2                         # Tuples are immutable
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    T[0] = 2                         
TypeError: 'tuple' object does not support item assignment

>>> T = (2,) + T[1:]                 # Make a new tuple for a new value
>>> T
(2, 2, 3, 4)

## Like lists and dictionaries, tuples support mixed types and nesting, but
## they don't grow and shrink because they are immutable
## NOTE:  The parenthesis enclosing a tuple's items can usually be omitted
## as follows:

>>> T = 'spam', 3.0, [11, 22, 33]
>>> T
('spam', 3.0, [11, 22, 33])

>>> T[1]
3.0

>>> T[2][1]
22

>>> T.append(4)
Traceback (most recent call last):
  File "<pyshell#313>", line 1, in <module>
    T.append(4)
AttributeError: 'tuple' object has no attribute 'append'

## Why Tuples?
""" So why have a type that is like a list, but supports fewer operations?
Their immutability is the whole point.  If you pass a collection of objects
around your program as a list, it can be changed anywhere.  If you use a
tuple, it cannot.  Consequently, tuples provide a sort of integrity constraint.
"""

