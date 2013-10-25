"""
Python3 Object Types

Everything in Python is an Object.
Python Programs can be decomposed into modules, statements, expressions, and
objects.

1. Programs are composed of modules.
2. Modules contain statements.
3. Statements contain expressions.
4. Expressions create and process objects

Object Type						Example
-----------						---------------------------------------------------
Numbers							1234, 3.14159, 3 + 4j, Ob111, Decimal(), Fraction()
Strings							'spam', "Bob's", b'a\x01c', u'sp\xc4m'
Lists							[1, [2, 'three'], 4.5], list(range(10))
Dictionaries					{'food':'spam', 'taste':'yum'}, dict(hours=10)
Tuples							(1,'spam', 4, 'U'), tuple('spam'), namedtuple
Files							open('eggs.txt'), open(r'C:\ham.bin', 'wb')
Sets							set('abc'), {'a', 'b', 'c'}
Other core types				Booleans, types, None
Program unit types				Functions, modules, classes
Implementation related types	Compiled code, stack tracebacks

Once you create an object, you bind its operation set for all time.
This means that Python is dynamically typed.
It is also strongly typed (you can only do to an object what it allows)

Immutable Objects
------------------------
Numbers, Strings, Tuples

Mutable Objects
------------------------
Lists, Dictionaries, Sets


"""
