#!/usr/bin/python3
""" defines a function that divides matrices """

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and returns the
    resulting matrix with elements rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise ValueError("all rows in the matrix must have the same length")
    
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("all elements in the matrix must be integers or floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be an integer or a float")
    
    if div == 0:
        raise ValueError("divisor cannot be zero")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    
    return new_matrix
