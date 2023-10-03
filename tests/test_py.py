from myproject import multiply_py


def test_multiply_py():
    """
    Test the Python implementation of the matrix multiplication.
    """
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    result = multiply_py(a, b)
    assert result == [[19, 22], [43, 50]]
