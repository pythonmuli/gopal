Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x='mani'
>>> x
'mani'
>>> x+"vicky"
'manivicky'
>>> x[0]
'm'
>>> x[1]
'a'
>>> x[0,1,2]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x[0,1,2]
TypeError: string indices must be integers
>>> x[-6]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x[-6]
IndexError: string index out of range
>>> x[0:2]
'ma'
>>> x[0:1]
'm'
>>> x[0:3]
'man'
>>> 
