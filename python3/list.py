"""
Python3 Notes on Lists

The Python list object is the most general sequence provided by the language.
Lists are positionally ordered collections of arbitrary typed objects, and
they have no fixed size.  They are also mutable -- unlike strings, lists can
be modified in place by assignment to offsets as well as a variety of list
method calls.
"""

## Sequence Operations

>>> L = [123, 'spam', 1.23]    # A list of three different-type objects
>>> len(L)                     # Number of items in the list
3

''' We can index, slice, and so on, just as for strings: '''

>>> L[0]                         # Indexing by position
123
>>> L[:-1]                       # Slicing a list returns a new list
[123, 'spam']
>>> L + [4,5,6]                  # Concat make a new list too
[123, 'spam', 1.23, 4, 5, 6]
>>> L * 2                        # Repeat make a new list too
[123, 'spam', 1.23, 123, 'spam', 1.23]
>>> L                            # We're not changing the original list
[123, 'spam', 1.23]

## Type-Specific Operations

>>> L.append('NI')               # Growing: add object at end of list
>>> L
[123, 'spam', 1.23, 'NI']
>>> 
>>> L.pop(2)                     # "del L[2]" delete from a list too
1.23
>>> L
[123, 'spam', 'NI']
>>> del L[2]                     # Can also use del
>>> L
[123, 'spam']
>>> L.append('NI')

## Most list methods change the list in place
>>> M = ['bb', 'aa', 'cc']
>>> M.sort()
>>> M
['aa', 'bb', 'cc']
>>> M.reverse()
>>> M
['cc', 'bb', 'aa']

## List have Bounds checking

>>> L
[123, 'spam', 'NI']
>>> L[99]
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    L[99]
IndexError: list index out of range
>>> L[99] = 1
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    L[99] = 1
IndexError: list assignment index out of range

## Lists support arbitrary Nesting
>>> M = [[1, 2, 3],          # A 3x3 matrix, as nested lists
         [4, 5, 6],          # Code can span lines if bracketed
         [7, 8, 9]]
>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> M[1]                     # Get row 2
[4, 5, 6]
>>> M[1][2]                  # Get row 2, then get item 3 within the row
6

## List Comprehensions
>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> col2 = [row[1] for row in M]        # Collect the items in column 2
>>> col2
[2, 5, 8]

>>> M                                   # The matrix is unchanged
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> [row[1] + 1 for row in M]           # Add 1 to each item in column 2
[3, 6, 9]

>>> [row[1] for row in M if row[1] % 2 == 0]  # Filter out odd items
[2, 8]

>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> diag = [M[i][i] for i in [0,1,2]]    # Collect a diagonal from matrix
>>> diag
[1, 5, 9]

>>> doubles = [c * 2 for c in 'spam']    # Repeat characters in a string
>>> doubles
['ss', 'pp', 'aa', 'mm']

>>> ''.join(doubles)
'ssppaamm'

>>> list(range(4))                       # 0..3 (list() required in 3.X)
[0, 1, 2, 3]

>>> list(range(-6,7,2))                  # -6 to 6 by 2
[-6, -4, -2, 0, 2, 4, 6]

>>> [[x**2, x**3] for x in range(4)]     # Multiple values
[[0, 0], [1, 1], [4, 8], [9, 27]]

>>> [[x, x/2, x*2] for x in range(-6,7,2) if x > 0]
[[2, 1.0, 4], [4, 2.0, 8], [6, 3.0, 12]]


## Comprehensions can be used to create generators that produce results
## on demand

>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> G = (sum(row) for row in M)          # Create a generator of row sums

>>> next(G)                              # iter(G) not required here
6

>>> next(G)                              # Run the iteration protocol next
15

>>> next(G)
24

## map can do similar work, by generating the results of running items through
## a function, one at a time and on request.

>>> list(map(sum, M))                   # Map sum over items in M
[6, 15, 24]

## Comprehensions can also be used to create sets and dictionaries:

>>> {sum(row) for row in M}                   # Create a set of row sums
{24, 6, 15}

>>> {i:sum(M[i]) for i in range(3)}           # Create key/value table of row sums
{0: 6, 1: 15, 2: 24}

## lists, sets, dictionaries, and generators can all be built with
## comprehensions in 3.X and 2.7:

>>> [ord(x) for x in 'spaam']             # List of character ordinals
[115, 112, 97, 97, 109]
>>> {ord(x) for x in 'spaam'}             # Sets remove duplicates
{112, 97, 115, 109}
>>> {x:ord(x) for x in 'spaam'}           # Dictionary keys are unique
{'s': 115, 'p': 112, 'a': 97, 'm': 109}
>>> (ord(x) for x in 'spaam')             # Generator of values
<generator object <genexpr> at 0x1015050f0>


