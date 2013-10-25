"""
Python3 Notes on Fraction type
"""

>>> from fractions import Fraction   # Fractions: numerator + denominator

>>> f = Fraction(2,3)

>>> f + 1
Fraction(5, 3)

>>> f + Fraction(1,2)
Fraction(7, 6)
