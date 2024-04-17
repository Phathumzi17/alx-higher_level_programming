#!/usr/bin/python3
'''Module for attributes_methods function.'''

def attributes_methods(ob):
    '''Lists attributes and methods of an object.
    Args:
        ob: The object to list.

    Returns:
        list: List of attributes and methods.
    '''
    return dir(ob)
