from typing import List
import math

Vector = List[float]


def add(v1: Vector, v2: Vector) -> Vector:
    """Adds v1 vector to the v2 if the length of them are the same"""
    assert len(v1) == len(v2), "length of vectors must be the same"

    return [x + y for x, y in zip(v1, v2)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9], "error adding vectors"


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sum a list of vectors"""
    assert len(vectors) > 0, "vector list is empty"

    num_of_elements = len(vectors[0])
    assert all(
        len(i) == num_of_elements for i in vectors
    ), "not all vectors are in the same size"

    return [sum(vector[i] for vector in vectors) for i in range(num_of_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""

    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""

    n = len(vectors)

    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    """Dot operation on two vectors"""

    assert len(v) == len(w), "length of vectors are not equal"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + .... + v_n * v_n"""
    return dot(v, v)


assert sum_of_squares([1, 2, 3]) == 14


def magnitude(v: Vector) -> float:
    """Returns the magnitude - or length - of v"""
    return math.sqrt(sum_of_squares(v))


assert magnitude([3, 4]) == 5


def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))
