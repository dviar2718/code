"""
Python3 Notes on using Regular Expressions
"""
import re

## What if you need to split on more than one string?

>>> import re
>>> re.split('[/:]','/usr/home:lumberjack/bob')
['', 'usr', 'home', 'lumberjack', 'bob']

