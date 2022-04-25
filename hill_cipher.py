# This was made using information from the Grade 12 Specialist Maths textbook
from Matrix import Matrix

# Variables
MATRIX = Matrix((2, -1), (1, 5)) # the encipher matrix (must be 2x2)
MESSAGE = "IVWLAEDCOUEDVWKRYR" # must only have capital letters
DO_ENCIPHER = False # whether to encipher or decipher

def char_num(c: str):
    # A is defined as 1, Z is 0
    return ord(c) - 64

def num_char(n: int):
    return 'Z' if n == 0 else chr(n + 64)

# Modular multiplicative inverse
# This is a naive implementation in mod 26
def mod_inverse(n: int):
    for i in range(1, 26):
        if (i * n) % 26 == 1:
            return i
    raise Exception("no inverse")

def cipher(A: Matrix, message: str):
    ciphered_message = ""
    for i, _ in enumerate(message):
        if i % 2 == 1: continue
        
        P = Matrix((char_num(message[i]),), (char_num(message[i + 1]),))
        result = (A @ P).affect_elements(lambda x: x % 26)
        ciphered_message += num_char(result.get_element(1, 1)) + num_char(result.get_element(2, 1))
    print(ciphered_message)

if DO_ENCIPHER:
    cipher(MATRIX, MESSAGE + (MESSAGE[-1] if len(MESSAGE) % 2 == 1 else ""))
else:
    a, b = MATRIX.elements[0]
    c, d = MATRIX.elements[1]
    A_ = (mod_inverse(a * d - b * c) * Matrix((d , -b), (-c, a))).affect_elements(lambda x: x % 26)
    cipher(A_, MESSAGE)