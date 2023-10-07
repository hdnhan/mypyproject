import numpy as np
import numpy.typing as npt


def fib(n: int) -> int:
    """Calculate the nth Fibonacci number.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def matmul(a: npt.NDArray, b: npt.NDArray) -> npt.NDArray:
    """Multiply two matrices.

    Args:
        a: The first matrix.
        b: The second matrix.

    Returns:
        The product of the two matrices.
    """
    # Check that the number of columns in a is equal to the number of rows in b.
    if a.shape[1] != b.shape[0]:
        raise ValueError(
            "The number of columns in a must be equal to the number of rows in b."
        )
    return np.matmul(a, b)
