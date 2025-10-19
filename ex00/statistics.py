def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calculates a list of numbers.
    """
    if not args:
        for key in kwargs:
            print("Error")
        return
    
    sorted_numbers = sorted(list(args))
    n = len(sorted_numbers)
    result = 0
    for operation in kwargs.values():
        if operation == "mean":
            result += sum(sorted_numbers) / n
            print(f"mean : {result}")
        
        elif operation == "median":
            index = int((n - 1) / 2)
            if n % 2 != 0:
                result = sorted_numbers[index]
                print(f"median : {result}")
            else:
                result = (sorted_numbers[index] + sorted_numbers[index + 1]) / 2
                print(f"median : {result}")
        
        elif operation == "quartile":
            index_q1 = int(n * 0.25)
            index_q2 = int(n * 0.75)
            result = [float(sorted_numbers[index_q1]), float(sorted_numbers[index_q2])]
            print(f"quartile : {result}")
        
        elif operation == "std":
            pass
            
        elif operation == "var":
            mean = 0
            if n < 2:
                print("Error: Variance requires at least two data points to be meaningful.")
            mean = mean + sum(sorted_numbers) / n
            sum_of_squared_differences = sum([(x - mean) ** 2 for x in sorted_numbers])
            variance = sum_of_squared_differences / n
            print(f"variance : {variance}")
                    
        else:
            print("ERROR")
        
