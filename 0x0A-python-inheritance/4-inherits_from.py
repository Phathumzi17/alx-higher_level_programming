#!/usr/bin/python3
'''Module for `inherits_from` function.'''

def inherits_from(obj, a_class):
    '''Checks if an object is an instance of a subclass of the specified class.'''
    return isinstance(obj, a_class) and type(obj) != a_class
