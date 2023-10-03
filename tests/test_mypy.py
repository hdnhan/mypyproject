import numpy as np
from myproject import multiply_numpy


def test_multiply_numpy():
    """
    Test the NumPy implementation of the matrix multiplication.
    """
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    result = multiply_numpy(a, b)
    assert np.all(result == np.array([[19, 22], [43, 50]]))
