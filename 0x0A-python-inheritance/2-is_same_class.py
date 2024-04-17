#!/usr/bin/python3
'''Module for `is_same_class` function.'''

def is_same_class(obj, a_class):
    '''Checks if an object is an instance of the specified class.'''
    return type(obj) == a_class
