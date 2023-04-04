#!/usr/bin/python3
"""
This function divides a matrix by the indicated integer
"""


def matrix_divided(matrix, div):
    """This function divides the matrix of lists
    Args:
        matrix: the matrix of lists
        div: the number which the matrix will be divided
    Returns:
        returns the matrix of floats rounded to two decimal places
    Raises:
        TypeError: the values of the matrix must be integers or floats
        TypeError: the number of rows of the matrix must be equal size
        TypeError: div must be an integer or float
        ZeroDivisionError: div must not be zero
        """
    new_matrix = []
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(value, int) or isinstance(value, float))
                    for value in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix list of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
