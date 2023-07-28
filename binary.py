# Functions for converting to and from various binary formats


def from_unsigned(binary: str) -> int:
    return int(binary, 2)


def from_signed_magnitude(binary: str) -> int:
    return from_unsigned(binary[1:]) * (1 if binary[0] == "0" else -1)


def from_ones_complement(binary: str) -> int:
    neg = -(2**(len(binary) - 1) - 1) if binary[0] == "1" else 0
    return from_unsigned(binary[1:]) + neg


def from_twos_complement(binary: str) -> int:
    """
    >>> from_twos_complement('00000000')
    0
    >>> from_twos_complement('11111111')
    -1
    """
    neg = -(2**(len(binary) - 1)) if binary[0] == "1" else 0
    return from_unsigned(binary[1:]) + neg


def from_excess(binary: str) -> int:
    """
    >>> from_excess('0000')
    -8
    >>> from_excess('1000')
    0
    """
    return from_unsigned(binary) - 2**(len(binary) - 1)


def to_unsigned(n: int, bits: int = 8) -> str:
    """
    >>> to_unsigned(73)
    '01001001'
    """
    return bin(n)[2:].rjust(bits, "0")


def to_signed_magnitude(n: int, bits: int = 8) -> str:
    """
    >>> to_signed_magnitude(47, 8)
    '00101111'
    >>> to_signed_magnitude(-47, 8)
    '10101111'
    """
    return ("1" if n < 0 else "0") + to_unsigned(abs(n), bits=bits - 1)


def to_ones_complement(n: int, bits: int = 8) -> str:
    """
    >>> to_ones_complement(-3, bits=4)
    '1100'
    >>> to_ones_complement(-127)
    '10000000'
    >>> to_ones_complement(127)
    '01111111'
    """
    return to_unsigned(n if n >= 0 else 2**bits + n - 1, bits=bits)


def to_twos_complement(n: int, bits: int = 8) -> str:
    """
    >>> to_twos_complement(0)
    '00000000'
    >>> to_twos_complement(-1)
    '11111111'
    >>> to_twos_complement(-128)
    '10000000'
    """
    return to_unsigned(n if n >= 0 else 2**bits + n, bits=bits)


def to_excess(n: int, bits: int = 8) -> str:
    """
    >>> to_excess(47)
    '10101111'
    >>> to_excess(-47)
    '01010001'
    """
    return to_unsigned(n + 2**(bits - 1), bits=bits)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
