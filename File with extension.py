Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> filename = input("Input the filename: ")
Input the filename: abc.py
>>> name,ext = os.path.splitext(filename)
>>> ext_with_dot =ext[1:]
>>> print (ext)
.py
>>> 