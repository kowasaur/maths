from operator import add, sub, mul
from functools import reduce
from typing import SupportsRound, Union

Number = Union[float, int]

def tmap(func: "function", *iterables):
    return tuple(map(func, *iterables))

# Treat column/row as vector
def dot(t1: tuple, t2: tuple) -> Number:
    assert len(t1) == len(t2), "Length of row and column must be same"
    return reduce(lambda sum, pair: sum + pair[0] * pair[1], zip(t1, t2), 0)

def numlen(num: Number):
    return len(str(num))

# For printing
def pad_cell(element: float, column: "tuple[float]") -> str:
    cell = str(element)
    padding_amount = numlen(max(column, key=lambda k: numlen(k))) - len(cell)
    return padding_amount * " " + cell

class Matrix:
    def __init__(self, *elements: "tuple[float]"):
        assert all(
            len(row) == len(elements[0]) for row in elements
        ), "All rows must have the same number of columns"

        # TODO: Maybe make private and create getter instead
        self.elements = elements
        # TODO: Maybe make these functions instead so if elements change these change
        self.rows = len(elements)
        self.columns = len(elements[0])
        self.order = f"{self.rows} x {self.columns}"
        self.isSquare = self.rows == self.columns
        self.isColumn = self.columns == 1
        self.isRow = self.rows == 1
    
    # Display in grid
    def __repr__(self) -> str:
        return "\n".join(map(
            lambda row: " ".join(
                pad_cell(element, self.get_column(i + 1)) for i, element in enumerate(row)
            ),
            self.elements
        ))

    def __eq__(self, other: "Matrix"):
        return self.elements == other.elements

    def same_order(self, other: "Matrix"):
        return self.order == other.order

    def _combine(self, other: "Matrix", operation: "function"):
        assert self.same_order(other), "Order must be same"
        return Matrix(*tmap(
            lambda s, o: tmap(operation, s, o),
            self.elements, other.elements
        ))

    # Affect every element in the matrix by a function
    def affect_elements(self, func: "function", *args):
        return Matrix(*[tuple(
            func(column, *args) for column in row
        ) for row in self.elements])

    def __add__(self, other: "Matrix"):
        return self._combine(other, add)

    def __sub__(self, other: "Matrix"):
        return self._combine(other, sub)

    def __mul__(self, scalar: float):
        return self.affect_elements(mul, scalar)

    def __rmul__(self, other: float):
        return self * other

    def __pow__(self, scalar: float):
        result = self
        for _ in range(1, scalar):
            result @= self
        return result

    # @ operator
    def __matmul__(self, other: "Matrix"):
        assert self.columns == other.rows
        return Matrix(*tmap(
            lambda r: tmap(
                lambda c: dot(self.get_row(r), other.get_column(c)), 
                range(1, other.columns + 1)
            ),
            range(1, self.rows + 1)
        ))

    def __round__(self, n: SupportsRound = None):
        return self.affect_elements(round, n)

    def determinant(self) -> Number:
        assert self.isSquare, "Determinant of non square does not exist"
        if self.order == "2 x 2":
            e = self.get_element
            return e(1, 1) * e(2, 2) - e(1, 2) * e(2, 1)
        # Not 2 x 2
        sum = 0
        for i, n in enumerate(self.elements[0]):
            sum += (-1 if i % 2 else 1) * n * self.remove_row(1).remove_column(i + 1).determinant()
        return sum

    def get_element(self, row: int, column: int):
        assert row > 0 and column > 0, "row and column must be positive"
        return self.elements[row - 1][column - 1]

    def get_row(self, row: int):
        assert row > 0, "row must be positive"
        assert row <= self.rows, "row out of range"
        return self.elements[row - 1]

    def get_column(self, column: int):
        assert column > 0, "column must be positive"
        assert column <= self.columns, "column out of range"
        return tuple(map(lambda r: r[column - 1], self.elements))

    # Return copy of self with specified row removed
    def remove_row(self, row: int):
        # https://stackoverflow.com/a/25004389/13837629
        new_elements = self.elements[:row - 1] + self.elements[row:]
        return Matrix(*new_elements)
    
    # Return copy of self with specified column removed
    def remove_column(self, column: int):
        new_elements = [row[:column - 1] + row[column:] for row in self.elements]
        return Matrix(*new_elements)

    def transpose(self):
        new_elements = [tuple(
            self.elements[r][c] for r in range(0, self.rows)
        ) for c in range(0, self.columns)]
        return Matrix(*new_elements)

    #region Special Matrices

    def zero(self):
        return self * 0
    
    def identity(self):
        assert self.isSquare, "Identity for non-square matrix not supported"
        return Matrix(*tmap(
            lambda i: tmap(lambda j: 1 if i == j else 0, range(0, self.rows)),
            range(0, self.rows)
        ))

    #endregion

if __name__ == "__main__":
    m = Matrix(
        (2, 3, 7), 
        (4, 5, 3)
    )
    n = Matrix(
        (1, 2),
        (3, 4),
        (6, 4)
    )
    s = Matrix(
        (2, 1, 5, 2),
        (5, 2, 3, 2),
        (8, 3, 4, 2),
        (8, 3, 4, 4)
    )

    a = Matrix(
        (5, 2),
        (3, 4)
    )
    print(a * 2)
