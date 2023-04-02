#!/usr/bin/python3
""" This module contains a function, add_integer,that adds two integers
     or floats and returns the result as an integer
"""

def add_integer(a, b=98):
    """ if the values of a and b ar not a float or integer,
        a TypeError is returned 
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b,(int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b)) 
