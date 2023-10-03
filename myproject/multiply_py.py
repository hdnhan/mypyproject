from typing import List


def multiply_py(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Multiply two matrices together.

    Parameters
    ----------
    a : List[List[float]]
        First matrix to multiply.
    b : List[List[float]]
        Second matrix to multiply.

    Returns
    -------
    List[List[float]]
        Result of multiplying a and b.

    """
    # Check that the number of columns in a is equal to the number of rows in b.
    if len(a[0]) != len(b):
        raise ValueError(
            "The number of columns in a must be equal to the number of rows in b."
        )

    # Initialize the result matrix.
    result: List[List[float]] = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    # Multiply the matrices.
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result
