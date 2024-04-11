#!/usr/bin/python3dd_integer` Module
==========================

This module provides a function `add_integer` that adds two numbers.

Using `add_integer`
-------------------

Importing the function from the module:
>>> add_integer = __import__('0-add_integer').add_integer

Addition Examples:
>>> add_integer(4, 4)
8

>>> add_integer(-40, -60)
-100

>>> add_integer(-10, 5)
-5

>>> add_integer(4.0, 4.0)
8

>>> add_integer(2)
100

Handling Invalid Inputs:
>>> add_integer(10, "hello")
Traceback (most recent call last):
    ...
TypeError: b must be an integer

>>> add_integer(None)
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer('1', 5)
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer('abc', 'def')
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer((1, 2, 3))
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer(10, [0])
Traceback (most recent call last):
    ...
TypeError: b must be an integer

>>> add_integer("Add")
Traceback (most recent call last):
    ...
TypeError: a must be an integer

Special Cases:
>>> add_integer(float('inf'), 0)
Traceback (most recent call last):
    ...
OverflowError: cannot convert float infinity to integer

>>> add_integer(float('inf'), float('-inf'))
Traceback (most recent call last):
    ...
OverflowError: cannot convert float infinity to integer

>>> add_integer(0, float('nan'))
Traceback (most recent call last):
    ...
ValueError: cannot convert float NaN to integer
"""this module contain a function that adds to integers or float"""


def add_integer(a, b=98):
    """Returns addition of a and b.

    Raises:
        TypeError: If either of a or b is not integer  or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))i
