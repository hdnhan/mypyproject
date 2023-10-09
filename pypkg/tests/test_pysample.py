import numpy as np
from pysample import fib, matmul


def test_fib():
    n = 10
    expected = 55
    result = fib(n)
    assert expected == result


def test_matmul():
    a = np.random.rand(3, 4)
    b = np.random.rand(4, 5)

    expected = np.matmul(a, b)
    result = matmul(a, b)
    assert np.allclose(expected, result)
