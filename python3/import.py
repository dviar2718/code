"""
Python3 Notes
When you import a module, the code is only run once.  If
you want to force it to run the module again, use reload
this is built-in in Python 2.X but requires an import in 3.X

The move in 3.X was likely motivated by issues involving reload and from
statements.  Names loaded with a from are not directly updated by a reload,
but names accessed with an import are.  If your names don't seem to change
after a reload, try using import module and module.attribute name references
instead.

The reload function expects the name of an already loaded module object,
so you have to have successfully imported a module once before you reload
it.

Note:  Reloads aren't transitive.  Reloading a module reloads that module
only, not any modules it may import.
"""

import input

from imp import reload

reload(input)

##>>> import input
##>>> from imp import reload
##>>> reload(input)
##Please Enter a number: 1.2345
##Your number was 1.23
##<module 'input' from '/Users/dlviar/code/python2/input.pyc'>

"""
You can also run code from a file by using exec
"""

exec(open('input.py').read())

##Please Enter a number: 123.456
##Your number was 123.46
