"""
Python3 basic notes on creating classes (i.e. user defined types)
"""

## Create a new type to model an employee
>>> class Worker:
	def __init__(self, name, pay):          # Initialize when created
		self.name = name
		self.pay  = pay
	def lastName(self):
		return self.name.split()[-1]    # Split string on blanks
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)     # Update pay in place

		
"""
This class defines a new kind of object that will have name and pay attributes
(i.e. state information), as well as two bits of behavior coded as functions
(normally called methods).  Calling the class like a function generates
instances of our new type, and he class's methods automatically recieve the
instance being processed by a given method call (in the self argument):
"""
>>> bob = Worker('Bob Smith', 50000)            # Make two instances
>>> sue = Worker('Sue Jones', 60000)

>>> bob.lastName()                              # Call method: bob is self
'Smith'

>>> sue.lastName()                              # sue is the self subject
'Jones'

>>> sue.giveRaise(.10)                          # updates sue's pay
>>> sue.pay
66000.0
