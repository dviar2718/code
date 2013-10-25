"""
Python3 notes on the Set data type
Sets are neither mappings nor sequences.  They are unordered collections of
unique and immutable objects.
"""
>>> X = set('spam')              # Make a set out of a sequence in 2.X and 3.X

>>> Y = {'h', 'a', 'm'}          # Make a set with set literals in 3.X and 2.7
>>> X, Y                         # A tuple of two sets without parentheses
({'s', 'p', 'a', 'm'}, {'h', 'a', 'm'})

>>> X & Y                        # Intersection
{'a', 'm'}

>>> X | Y                        # Union
{'h', 'm', 's', 'p', 'a'}

>>> X - Y                        # Difference
{'s', 'p'}

>>> Y - X
{'h'}

>>> X > Y                        # Superset
False

>>> {n ** 2 for n in [1,2,3,4]}  # Set comprehensions in 3.X and 2.7
{16, 1, 4, 9}

>>> list(set([1,2,1,3,1]))       # Filtering out duplicates (possibly reordered)
[1, 2, 3]

>>> set('spam') - set('ham')     # Finding differences in collections
{'s', 'p'}

>>> set('spam') == set('asmp')   # Order-neutral equality tests
True

>>> 'p' in set('spam')           # membership test
True

>>> 'p' in 'spam'
True

>>> 'ham' in ['eggs', 'spam', 'ham']
True
