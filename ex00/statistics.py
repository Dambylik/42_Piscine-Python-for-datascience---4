from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculates a list of numbers.
    """
    if not args:
        if kwargs:
            for key in kwargs:
                print("ERROR")
        return

    sorted_numbers = sorted(list(args))
    n = len(sorted_numbers)

    for operation in kwargs.values():
        if operation == "mean":
            mean = sum(sorted_numbers) / n
            print(f"mean : {mean}")

        elif operation == "median":
            if n % 2 == 1:
                median = sorted_numbers[n // 2]
            else:
                median = (sorted_numbers[n // 2 - 1] +
                          sorted_numbers[n // 2]) / 2
            print(f"median : {median}")

        elif operation == "quartile":
            index_q1 = int(0.25 * (n - 1))
            index_q2 = int(0.75 * (n - 1))
            quart = [float(sorted_numbers[index_q1]),
                     float(sorted_numbers[index_q2])]
            print(f"quartile : {quart}")

        elif operation == "std":
            if n < 2:
                print("ERROR")
                continue
            mean_data = sum(sorted_numbers) / n
            squared_diffs = sum((x - mean_data) ** 2 for x in sorted_numbers)
            variance = squared_diffs / n
            stddev = variance ** 0.5
            print(f"std : {stddev}")

        elif operation == "var":
            if n < 2:
                print("ERROR")
                continue
            mean_data = sum(sorted_numbers) / n
            squared_diffs = sum((x - mean_data) ** 2 for x in sorted_numbers)
            variance = squared_diffs / n
            print(f"var : {variance}")

        else:
            continue
