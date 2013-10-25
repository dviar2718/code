"""
Python3 Notes:  How to find help

"""

## online help
## http://www.python.org/doc
## Quick Reference:
## for 2.7 only http://rgruet.free.fr/PQR27/PQR2.7.html
## http://rgruet.free.fr/#QuickRef

## dir() by itself lists all of the variables assigned in the caller's scope
dir()

## If S is a string
S = 'Hello'
## Find out what you can do to S:
dir(S)
## i.e. dir(S) list all the attributes available for any object passed to it.
print("dir(S) where S is a string gives:")
print(dir(S))

## You can also use
dir(str)

## What are all the double underscores (e.g. __add__)?
## They represent the implementation of the string object and are available
## to support customization.  For example, __add__ is what actually
## does concatenation.  Here's an example:
S.__add__('NI!')  #Don't do this, it may be slower than +
"""
>>> S + 'NI!'
'HelloNI!'
>>> S.__add__('NI!')
'HelloNI!'
>>>
"""

## Then when you find something you want to know more about (e.g. isdigit)
help(str.isdigit)
help(S.isdigit)

## help is one of a handful of interfaces to a system of code that ships
## with Python known as PyDoc -- a tool for extracting documentation from
## objects.

## What is the difference between help() and dir()?
## consider the following:
"""
>>> dir(str.replace)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__objclass__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

>>> help(str.replace)
Help on method_descriptor:

replace(...)
    S.replace(old, new[, count]) -> str
    
    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.

>>>
"""

