"""
Python3 notes on Booleans and None Type

Booleans (with predefined True and False objects) are essentially just the
integers 1 and 0 with custom display logic.

None is a special placeholder object used to initialize names and objects.
"""

>>> 1 > 2, 1 < 2                     # Booleans
(False, True)

>>> bool('spam')                     # Object's Boolean value
True

>>> bool('0')
True

>>> bool(0)
False

>>> X = None                         # None placeholder
>>> print(X)
None
>>> X

>>> L = [None] * 5                   # Initialize a list of 5 Nones
>>> L
[None, None, None, None, None]
