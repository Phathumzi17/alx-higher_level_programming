#!/usr/bin/python3
'''Module for `Rectangle` class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Subclass representing a rectangle.'''
    def __init__(self, width, height):
        '''Constructor method.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Returns the area of the rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''String representation of the rectangle.'''
        return f"[Rectangle] {self.__width}/{self.__height}"
