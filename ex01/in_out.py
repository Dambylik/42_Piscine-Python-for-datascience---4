def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return x raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that repeatedly applies function to x."""
    count = 0

    def inner() -> float:
        nonlocal x, count
        count += 1
        x = function(x)
        return x
    return inner
