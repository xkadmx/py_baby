Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.pen()
>>> t.forward(50)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.forward(50)
AttributeError: 'dict' object has no attribute 'forward'
>>> from turtle import *
>>> fd (100)
>>> fd(100)
>>> ld(50)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ld(50)
NameError: name 'ld' is not defined
>>> turtles
<function turtles at 0x05E2EDB0>
>>> shape("turtle")
>>> pencolor("red")
>>> 
