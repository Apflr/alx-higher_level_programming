#!usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Parameters:
        matrix (list of lists): The matrix to be printed. Defaults to an empty list.

    Returns:
        None
    """
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()  # Move to the next line after printing each row
