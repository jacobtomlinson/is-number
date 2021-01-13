def is_number(in_value):
    """Checks if a value is a valid number.

    Parameters
    ----------
    in_value
        A variable of any type that we want to check is a number.

    Returns
    -------
    bool
        True/False depending on whether it was a number.

    Examples
    --------
    >>> is_number(1)
    True
    >>> is_number(1.0)
    True
    >>> is_number("1")
    True
    >>> is_number("1.0")
    True
    >>> is_number("Hello")
    False

    You can also pass more complex objects, these will all be ``False``.

    >>> is_number({"hello": "world"})
    False
    >>> from datetime import datetime
    >>> is_number(datetime.now())
    False

    Even something which contains all numbers will be ``False``, because it is not itself a number.

    >>> is_number([1, 2, 3, 4])
    False

    """
    try:
        float(in_value)
        return True
    except (ValueError, TypeError):
        return False
