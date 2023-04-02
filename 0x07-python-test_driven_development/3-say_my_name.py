#!/usr/bin/python3
""" a function that prints a name"""

def say_my_name(first_name, last_name=""):
    """
    Prints a message with the given first name and last name.

    Args:
        first_name (str): The first name to include in the message.
        last_name (str): The last name to include in the message.

    Raises:
        AssertionError: If either first_name or last_name is not a string.

    Returns:
        None.
    """
    assert type(first_name) == str, "first_name must be a string"
    assert type(last_name) == str, "last_name must be a string"
    
    print(f"My name is {first_name} {last_name}")
