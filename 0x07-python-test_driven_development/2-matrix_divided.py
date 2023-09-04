#!/usr/bin/python3
"""
This module provides a function for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if each row of the matrix doesn't have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for idx in range(len(matrix)):
        new_row = []
        for element in matrix[idx]:
            if (
                not isinstance(element, (int, float)) or
                isinstance(element, bool)
            ):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of " +
                    "integers/floats"
                    )
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
