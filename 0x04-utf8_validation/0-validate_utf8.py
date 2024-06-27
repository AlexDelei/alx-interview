#!/usr/bin/python3
"""
Unicode Transformation Format (UTF-8)
validation
"""


def validUTF8(data):
    """
    UTF-8 is the most popular encoding system and it's
    work is to translate any unicode character to a 
    matching unique binary string and can also translate
    the binary string back to a unicode character.
    """
    try:
        byte_data = bytes(data) # converting all data into binary strings
        # so that the encoding system can work on them
        byte_data.decode('utf-8')
    except (UnicodeDecodeError, ValueError):
        return False
    return True
