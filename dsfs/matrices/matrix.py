from typing import List, Tuple, Callable

Vector = List[float]
Matrix = List[List[float]]

A = [[1.0, 2.0], [3.0, 4.0], [5, 0, 6.0]]

B = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]


def shape(m: Matrix) -> Tuple[int, int]:
    """Gets the shape of a matrix"""
    num_rows = len(m)
    num_cols = len(m[0])
    return num_rows, num_cols


assert shape(A) == (3, 2), "shape of matrix does not match"


def get_row(m: Matrix, i: int) -> Vector:
    """Gets row i of matrix"""
    return m[i]


def get_col(m: Matrix, j: int) -> Vector:
    """Gets the column j of matric m"""
    return [s[j] for s in m]


def make_matrix(
    num_rows: int, num_cols: int, entry_func: Callable[[int, int], float]
) -> Matrix:
    """Returns a matrix with num of rows and cols, with elements using a def provided"""
    return [[entry_func(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Returns the identity matrix with n rows and cols with 1 in the diagonal, and 0 in all other cells"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(3) == [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
