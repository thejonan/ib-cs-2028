def mat_mult(A: list[list], B: list[list]) -> list[list]:
    """
    Multiplies the two provided matrices, raising an exception if the sizes are incompatible.
    The format for the inputs and the output is the same - list of rows.

    Args:
        A (list[list]): The left matrix of the multiplication.
        B (list[list]): The right matrix of the multiplication.

    Returns:
        list[list]: The resulting matrix - A x B
    """
    raise


# DON'T EDIT BELOW THIS LINE

# Test 0: Incompatible matrix dimensions
try:
    # This catches the exception which is raised for incompatible matrices. Check the textbooks: B2.1.3
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [4.5, 5.6]]
    mat_mult(A, B)
except Exception:
    pass
else:
    assert False, "Expected an exception for incompatible matrices"

# Test 1: Multiplication of two square matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
assert mat_mult(A, B) == [[19, 22], [43, 50]]

# Test 2: Multiplication of two rectangular matrices (2x3 and 3x2)
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
assert mat_mult(A, B) == [[58, 64], [139, 154]]

# Test 3: Multiplication by an identity matrix
A = [[2, 3, 4], [5, 6, 7]]
B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert mat_mult(A, B) == A

# Test 4: Multiplication of a column by a row (3x1 and 1x2)
A = [[1], [2], [3]]
B = [[4, 5]]
assert mat_mult(A, B) == [[4, 5], [8, 10], [12, 15]]

# Test 5: Multiplication involving negative and fractional numbers
A = [[-1, 2.5], [0, -2]]
B = [[2, 4], [-2, 0.5]]
assert mat_mult(A, B) == [[-7, -2.75], [4, -1]]
