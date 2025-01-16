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
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
