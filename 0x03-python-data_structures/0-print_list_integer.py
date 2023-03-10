#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    prints integers ina list
    Args:
        my_list - list of integers default []
    """

    for num in my_list:
        print("{:d}".format(num))
