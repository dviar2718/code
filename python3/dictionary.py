"""
Python3 Notes on Dictionaries

Python Dictionaries are mappings.  They store objects by key instead of
by relative position.

Dictionaries are mutable.

"""

## Mapping Operations
>>> D = {'food':'Spam', 'quantity':4, 'color':'pink'}

>>> D['food']                 # Fetch value of key 'food'
'Spam'

>>> D['quantity'] += 1        # Add 1 to 'quantity' value

>>> D
{'color': 'pink', 'food': 'Spam', 'quantity': 5}

>>> D = {}

>>> D['name'] = 'Bob'         # Create keys by assignment
>>> D['job'] = 'dev'
>>> D['age'] = 40

>>> D
{'name': 'Bob', 'job': 'dev', 'age': 40}

>>> print(D['name'])
Bob

>>> bob1 = dict(name='Bob', job='dev', age=40)   # Keywords

>>> bob1
{'name': 'Bob', 'age': 40, 'job': 'dev'}

>>> bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))  # Zipping

>>> bob2
{'name': 'Bob', 'job': 'dev', 'age': 40}

## Nesting Dictionaries
>>> rec = {'name':{'first':'Bob', 'last':'Smith'},
           'jobs':['dev', 'mgr'],
           'age':40.5}

>>> rec['name']
{'first': 'Bob', 'last': 'Smith'}

>>> rec['name']                      # 'name' is a nested dictionary
{'first': 'Bob', 'last': 'Smith'}

>>> rec['name']['last']              # Index the nested dictionary
'Smith'

>>> rec['jobs']                      # 'jobs' is a nested list
['dev', 'mgr']

>>> rec['jobs'][-1]                  # Index the nested list
'mgr'

>>> rec['jobs'].append('janitor')    # Expand Bob's job description in place
>>> rec
{'name': {'first': 'Bob', 'last': 'Smith'}, 'jobs': ['dev', 'mgr', 'janitor'], 'age': 40.5}

## Missing Keys: if Tests
>>> D = dict(a=1, b=2, c=3)

>>> D
{'b': 2, 'c': 3, 'a': 1}

>>> D['e'] = 99                      # Assigning new keys grows dictionaries

>>> D
{'b': 2, 'c': 3, 'a': 1, 'e': 99}

>>> D['f']
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    D['f']
KeyError: 'f'

>>> 'f' in D
False
>>> if not 'f' in D:                 # Python's sole selection statement
	print('missing')

	
missing
>>> if not 'f' in D:
	print('missing')
	print('no, really...')       # Statement blocks are indented

	
missing
no, really...

>>> D
{'b': 2, 'c': 3, 'a': 1, 'e': 99}

>>> value = D.get('x', 0)            # Index but with a default
>>> value
0

>>> value = D['x'] if 'x' in D else 0  # if/else expression form
>>> value
0

## Sorting Keys: for loops
>>> Ks = list(D.keys())                # Unordered keys list
>>> Ks                                 # A list in 2.X, "view" in 3.X, so use list()
['b', 'c', 'a', 'e']

>>> Ks.sort()                          # Sorted keys list
>>> Ks
['a', 'b', 'c', 'e']

>>> for key in Ks:                     # Iterate through sorted keys
	print(key, '=>', D[key])

	
a => 1
b => 2
c => 3
e => 99

>>> D
{'b': 2, 'c': 3, 'a': 1, 'e': 99}

>>> for key in sorted(D):             # Use new 3.X function
	print(key, '=>', D[key])

	
a => 1
b => 2
c => 3
e => 99

>>> for c in 'spam':
	print(c.upper())

	
S
P
A
M

>>> x = 4
>>> while x > 0:
	print('spam!' * x)
	x -= 1

	
spam!spam!spam!spam!
spam!spam!spam!
spam!spam!
spam!

## Iteration and Optimation
""" An object is iterable if it is either a physically stored sequence in memory,
or an object that generates one item at a time in the context of an iteration
operation -- a sort of "virtual" sequence.

More formally, an object is iterable if it supports the iteration protocol,
i.e. it responds to the iter call with an object that advances in response
to next calls and raises an exception when finished producing values.

Examples:
- generator comprehension
- file objects
- range (new for 3.X)
- map (new for 3.X)
"""
## A list comprehension...
>>> squares = [x ** 2 for x in [1,2,3,4,5]]
>>> squares
[1, 4, 9, 16, 25]

## Can always be coded as a for loop
>>> squares = []
>>> for x in [1,2,3,4,5]:           # This is what a list comprehension does
	squares.append(x ** 2)

	
>>> squares
[1, 4, 9, 16, 25]

## NOTE:  The list comprehension will often run faster than a for loop
## A major rule of thumb in Python is to code for simplicity and readability
## first and worry about performance later, after your program is working, and
## after you've proved that there is a genuine performance concern.


