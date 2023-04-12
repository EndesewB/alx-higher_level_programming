#!/usr/bin/python3
"""pascal triangle in python module"""


def pascal_triangle(n):
    """function that returns the pascal triangle according to the formula"""
    if n <= 0:
        """if the dimension of triangle 0, returns empty list"""
        return []
    triangle = [[1]]
    """initializing the triangle"""
    for i in range(1, n):
        row = [1]
        """the first element of the row"""
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            """pascal triangle formula to calculate elements of entry"""
        row.append(1)
        triangle.append(row)
    return triangle
