#!/usr/bin/python3
'''Module for attributes_methods function.'''

def lookup(obj):
    '''Lists attributes and methods of an object.
    Args:
        ob(object): The object to list.

    Returns:
        list: List of attributes and methods.
    '''
    return dir(obj)
