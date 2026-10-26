"""Factorial program: iterative and recursive versions."""


def factorial_iterative(n):
    """Return n! using a loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Return n! using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"{num}! (loop)      = {factorial_iterative(num)}")
        print(f"{num}! (recursion) = {factorial_recursive(num)}")
    except ValueError as err:
        print("Error:", err)
