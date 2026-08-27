def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n cannot be negative")

    a, b = 1, 1

    for _ in range(n):
        a, b = b, a + b

    return a