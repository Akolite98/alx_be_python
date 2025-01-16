def safe_divide(numerator, denominator):
    """
    Perform division of two numbers, handling errors for zero division and non-numeric inputs.

    :param numerator: The numerator for the division.
    :param denominator: The denominator for the division.
    :return: A string message with the result or an error description.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Perform division and handle division by zero
        result = num / den

        # Format the result to match the expected output (e.g., "6.0" instead of "6.00")
        formatted_result = f"{result:.1f}" if result % 1 != 0 else f"{int(result)}"
        return f"The result of the division is {formatted_result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
