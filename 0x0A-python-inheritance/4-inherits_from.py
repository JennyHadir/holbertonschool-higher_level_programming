#!/usr/bin/python3
"""Check if instance"""


def inherits_from(obj, a_class):
    """Check if instance"""
    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    return False
