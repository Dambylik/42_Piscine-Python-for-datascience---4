from typing import Any


def callLimit(limit: int):
    "Limits the number of times a function can be called."
    count = 0

    def callLimiter(function):
        "Takes the target function you decorate."

        def limit_function(*args: Any, **kwds: Any):
            "Actually runs when you call the decorated function"
            "that’s where we count calls."
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call to many times")
        return limit_function

    return callLimiter
