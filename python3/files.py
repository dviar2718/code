"""
Python3 notes on File Objects

File objects are Python code's main interface to external files on your
computer.  They can be used to read and write text memos, audio clips,
Excel documents, saved email messages, etc...

Files are a core type, but they're something of an oddball.  There is no
specific literal syntax for creating them.  To create a file object, you
call the built-in open function, passing in an external filename and an
optional processing mode as strings.

"""

>>> f = open('data.txt', 'w')       # Make a new file in output mode ('w' is write)

>>> f.write('Hello\n')              # Write "Hello\n" into the file
6

>>> f.write('world\n')              # Return number of items written in Python 3.X
6

>>> f.close()                       # Close to flush output buffers to disk

"""
The code above creates a file in the current directory and writes text to it.
Note that the filename can be a full directory path if you need to access a
file elsewhere on your computer.
"""
>>> f = open('data.txt')            # 'r' (read) is the default processing mode

>>> text = f.read()                 # Read entire file into a string
>>> text
'Hello\nworld\n'

>>> print(text)
Hello
world

>>> for ch in text:                 # since text is a string, you can print line by line
	print(ch)

	
H
e
l
l
o


w
o
r
l
d


>>> text.split()                     # File content is always a string
['Hello', 'world']

>>> f.close()

## The best way to read a file is to not read it all, file provides an
## iterator that automatically reads line by line in for loops and other
## contexts:

>>> for line in open('data.txt'): print(line)

Hello

world

>>> for line in open('data.txt'): print(line, end='')

Hello
world

## How to find out more:

>>> f
<_io.TextIOWrapper name='data.txt' mode='r' encoding='US-ASCII'>

>>> dir(f)
['_CHUNK_SIZE', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']

>>> help(f.seek)
Help on built-in function seek:

seek(...)


## Binary Byte Files
"""
Python 3.X draws a sharp distinction between text and binary data in files:
text files represent content as normal str strings and perform Unicode encodings
and decodings automatically when writing and reading data, while binary files
represent content as a special bytes string and allow you to access file content
unaltered.  Python 2.X supports the same dichotomy, but doesn't impose it as
rigidly, and its tools differ.

For example, binary files are useful for processing media, accessing data
created by C programs, and so on.

Python's struct module can both create and unpack packed binary data, i.e.
raw bytes that record values that are not Python objects-- to be written
to a file in binary mode.
"""

>>> import struct

>>> packed = struct.pack('>i4sh', 7, b'spam', 8)   # Create packed binary data
>>> packed                                         # 10 bytes, not objects or text
b'\x00\x00\x00\x07spam\x00\x08'

>>> file = open('data.bin', 'wb')                  # Open binary output file
>>> file.write(packed)                             # Write packed binary data
10
>>> file.close()
>>> 

>>> data = open('data.bin', 'rb').read()           # Open/read binary data file
>>> data
b'\x00\x00\x00\x07spam\x00\x08'

>>> data[4:8]                                      # Slice bytes in the middle
b'spam'

>>> list(data)                                     # A sequence of 8-bit bytes
[0, 0, 0, 7, 115, 112, 97, 109, 0, 8]

>>> struct.unpack('>i4sh', data)                   # Unpack into objects again
(7, b'spam', 8)

## Unicode Text Files

>>> S = 'sp\xc4m'                                        # Non-ASCII Unicode text
>>> S
'spÄm'

>>> S[2]                                                 # Sequence of characters
'Ä'

>>> file = open('unidata.txt', 'w', encoding = 'utf-8')  # Write/encode UTF-8 text

>>> file.write(S)                                        # 4 characters written
4

>>> file.close()

>>> text = open('unidata.txt', encoding = 'utf-8').read() # Read/decode UTF-8 text
>>> text
'spÄm'

>>> len(text)                                             # 4 chars (code points)
4

## If needed you can also see what's truly stored in your file by stepping
## into binary mode:

>>> raw = open('unidata.txt', 'rb').read()               # Read raw encoded bytes
>>> raw
b'sp\xc3\x84m'

>>> len(raw)                                            # Really 5 bytes in UTF-8
5

## You can also encode and decode manually if you get Unicode data from a
## source other than a file

>>> text
'spÄm'

>>> text.encode('utf-8')                                # Manual encode to bytes
b'sp\xc3\x84m'

>>> raw
b'sp\xc3\x84m'

>>> raw.decode('utf-8')                                 # Manual decode to string
'spÄm'

>>> text.encode('latin-1')                              # Bytes differ in others
b'sp\xc4m'

>>> text.encode('utf-16')
b'\xff\xfes\x00p\x00\xc4\x00m\x00'

>>> len(text.encode('latin-1')), len(text.encode('utf-16'))
(4, 10)

>>> b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16') # But same string decoded
'spÄm'

## This all works more or less the same in Python 2.X, but Unicode string are
## coded and display with a leading 'u', byte strings don't require or show
## a leading 'b' and Unicode text files must be opened with codecs.open
## which accepts an encoding name just like 3.X's open and uses the special
## unicode string to represent content in memory.

>>> import codecs
>>> codecs.open('unidata.txt', encoding='utf8').read()  # 2.X: read/decode text
u'sp\xc4m'                                              # Get 'spÄm' in 3.X

>>> open('unidata.txt', 'rb').read()                    # 2.X: read raw bytes
'sp\xc3\x84m'                                           # Get b'sp\xc3\x84m' in 3.X

>>> open('unidata.txt').read()                          # 2.X: raw/undecoded too
'sp\xc3\x84m'                                           # Get error in 3.X

## Other File-Like Tools
""" Additional file-like tools include: pipes, FIFOs, sockets, keyed-access files,
persistent object shelves, descriptor-based files, relational and object-
oriented database interfaces, and more.
"""

