import numpy as np
import numpy.typing as npt


def multiply_numpy(a: npt.NDArray, b: npt.NDArray) -> npt.NDArray:
    """Multiply two matrices together.

    Parameters
    ----------
    a : npt.NDArray
        First matrix to multiply.
    b : npt.NDArray
        Second matrix to multiply.

    Returns
    -------
    npt.NDArray
        Result of multiplying a and b.

    """
    # Check that the number of columns in a is equal to the number of rows in b.
    if a.shape[1] != b.shape[0]:
        raise ValueError(
            "The number of columns in a must be equal to the number of rows in b."
        )

    # Multiply the matrices.
    return np.matmul(a, b)
