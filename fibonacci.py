"""Fibonacci program: generate the first n terms and find the nth term."""


def fibonacci_series(n):
    """Return a list with the first n Fibonacci numbers."""
    if n < 0:
        raise ValueError("Number of terms cannot be negative.")
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def fibonacci_nth(n):
    """Return the nth Fibonacci number (0-indexed) using recursion."""
    if n < 0:
        raise ValueError("Position cannot be negative.")
    if n < 2:
        return n
    return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)


if __name__ == "__main__":
    try:
        terms = int(input("How many Fibonacci terms? "))
        print("Series:", fibonacci_series(terms))
        if terms > 0:
            print(f"Term at position {terms - 1}:", fibonacci_nth(terms - 1))
    except ValueError as err:
        print("Error:", err)
