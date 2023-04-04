#!/usr/bin/python3

"""
This module defines a class rectangle
"""

class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """private instance attribute for the return value of width"""
        return self._width
    
    @width.setter
    def width(self, value):
        """
        setter for the instance atttribute of width
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value
    
    @property
    def height(self):
        """private instance attribute for the return value of height"""
        return self._height
    
    @height.setter
    def height(self, value):
        """ method that defines the height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value  
    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height
    
    def perimeter(self):
        """returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height) if self.width != 0 and self.height != 0 else 0
