# https://www.youtube.com/watch?v=094y1Z2wpJg

# Get next number
def collatz(n: int):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


# Return true once it reaches 1
def collatz_conjection(n: int) -> True:
    if n == 1:
        return True
    return collatz_conjection(collatz(n))


def main():
    max = int(input("Try until the number: "))
    # 1% increments unless max is less than 100 (then it's just every 5)
    increment = max // 100 if max >= 100 else 5
    for i in range(1, max + 1):
        collatz_conjection(i)
        # Show i every increment
        if i % increment == 0:
            print(i)
    print(f"All the numbers up to and including {max} return to 1")


if __name__ == "__main__":
    main()
