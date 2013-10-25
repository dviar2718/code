"""
Python3 Notes on the decimal type.
"""

>>> 1 / 3                        # Floating-point (add a .0 in Python 2.X)
0.3333333333333333

>>> (2/3) + (1/3)
1.0

>>> (2/3) + (1/2)
1.1666666666666665

>>> import decimal               # Decimals: fixed precision
>>> d = decimal.Decimal('3.141')

>>> d + 1
Decimal('4.141')

>>> decimal.getcontext().prec = 2

>>> decimal.Decimal('1.00') / decimal.Decimal('3.00')
Decimal('0.33')
