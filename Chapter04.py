#  Linear Algebra

from typing import List
from typing import Tuple
from typing import Callable
import math

Vector = List[float]

height_weight_age = [70,
                     170,
                     40]

grades = [95,
          80,
          75,
          62]

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1,2,3], [4,5,6]) == [5,7,9]

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be hte same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5,7,9], [4,5,6]) == [1,2,3]


#  We will also sometimes want to componentwise sum a list of vectors
#  that is, create a new vector whose first element is the sum of all
#  first elements, whose second element is the sum of all the
#  second elements, and so on
def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all the corresponding elements"""
    #  Check that vectors are not empty
    assert vectors, "no vectors provided!"

    #  Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Different size vectors!"

    # the i-th element of the reult is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]
assert vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16,20]


#  We'll also need to be able to multiply a vector by a scalar,
#  which we do simply by multiplying each element of the vector
#  by that number:
def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


#  This allows us to compute the componentwise means of a
#  list of (same sized) vectors:
def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2], [3,4], [5,6]]) == [3,4]


#  A less obvious tool is the dot product. The dot product
#  of two vectors is the sum of their componentwise products:
def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), ("Vectors must be same length!")

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32   #  1 * 4 + 2 * 5 + 3 * 6


#  Using this we cna easily compute a vector's sum of squares:
def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 ... + v_n * v_n"""
    return dot(v, v)

#  Which we can use to compute its magnitude (or length):
def magnitude(v: Vector) -> float:
    """Returns the magnitude (or lenght) of V"""
    return math.sqrt(sum_of_squares(v))     #  math.sqrt is the square root function

assert magnitude([3, 4]) == 5


#  We now have all the pieces we need to compute the distance between
#  two vectors.
def suared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n -w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))


#  A Matrix is a two dimensionanl collection of numbers.

#  Another type alias
Matrix = List[List[float]]

A = [[1, 2, 3],
     [4, 5, 7]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

def shape(A: Matrix) -> Tuple[int, int]:
    """Returns # of rows of A, # of columns of A"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1, 2, 3],
              [4, 5, 6]]) == (2, 3)

def get_row(A: atrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j]
            for A_i in A]

#  We'll also want to be able to create a matrix given
#  it's shape and a function for generating it's elements.
#  We can do this using a nested list comprehension.
def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """Returns a num_rows x num_cols matrix whose
     (i,j)-th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0 ,1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]

#  Matrices are important; for example, if you had the heights, weights,
#  and ages of 1,000 people you could put them in a 1,000 x 3 matrix:

