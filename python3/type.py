"""
Python3 Notes on the built in function type

aka "How to Break your code"
"""
>>> L = [1, 2, 3]

# In Python 2.X
>>> type(L)                      # Types: type of L is list type object
<type 'list'>

>>> type(type(L))                # Even types are objects
<type 'type'>

# In Python 3.X
>>> type(L)                      # Types: type of L is list type object
<class 'list'>

>>> type(type(L))                # Even types are objects
<class 'type'>

## code to check the types of the objects in your application
## Note:  Not a Pythonic way of doing things!

>>> if type(L) == type([]):      # Type testing, if you must...
	print('yes')

	
yes
>>> if type(L) == list:          # Using the type name
	print('yes')

	
yes
>>> if isinstance(L, list):      # Object-oriented tests
	print('yes')

	
yes

"""
Why is this a bad thing to do in Python?  By checking for specific types
in your code, you break its flexibility, i.e. you limit your code to working
on one type.  Perhaps your code could work on a whole range of types.
"""
