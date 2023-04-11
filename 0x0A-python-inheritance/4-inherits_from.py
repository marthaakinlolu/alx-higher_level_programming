#!/usr/bin/python3
""" 
Function that returns True/False if obj is an instance of a_clas
 """
    def inherits_from(obj, a_class):
    """returns false if obj is a_class, otherwise true"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
