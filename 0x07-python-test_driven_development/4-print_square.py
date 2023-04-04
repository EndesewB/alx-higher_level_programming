#!/usr/bin/python3
"""
The module that prints a square
"""

def print_square(size):
    """Returns the square of side size
    Args:
        size: size is the size length of the square
    Returns: the area filled by '#
        """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
