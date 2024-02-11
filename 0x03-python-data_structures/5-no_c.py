#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all occurrences of characters 'c' and 'C' from a string.

    Parameters:
        my_string (str): The original string.

    Returns:
        str: A new string with all occurrences of 'c' and 'C' removed.
    """
    new_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
