#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from creating new LockedClass attributes for 
    anything other than 'first_name' attributes.    
    """

    __slots__ = ["first_name"]
