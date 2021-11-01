from math import floor, sqrt


class Surd:
    def __init__(self, root: int, coefficient: int = 1) -> None:
        self.root = root
        self.coefficient = coefficient

    def __repr__(self) -> str:
        coefficient = self.coefficient
        if coefficient == 0 or self.root == 0:
            return "0"
        root = f"√{self.root}" if self.root != 1 else ""
        return f"{coefficient if coefficient != 1 else ''}{root}"

    def simplify(self) -> "Surd":
        root = self.root
        coefficient = self.coefficient
        max_square = floor(sqrt(root))
        # Try all numbers from max_square -> 2
        for i in range(max_square, 1, -1):
            if root % (i ** 2) == 0:
                root //= i ** 2
                coefficient *= i
        return Surd(root, coefficient)


def simplify_program():
    surd = Surd(int(input("√")))
    print(surd.simplify())


if __name__ == "__main__":
    simplify_program()
