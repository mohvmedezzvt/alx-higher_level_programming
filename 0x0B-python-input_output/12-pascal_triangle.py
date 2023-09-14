#!/usr/bin/python3
"""pascal triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = [1]
        for i in range(1, len(triangle[-1])):
            row.append(triangle[-1][i - 1] + triangle[-1][i])
        row.append(1)
        triangle.append(row)

    return triangle
