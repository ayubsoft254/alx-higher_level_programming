#!/usr/bin/python3
"""Defines an object attribute for lookup function."""


def lookup(obj):
    """Return a list of object's available attributes."""
    return (dir(obj))
