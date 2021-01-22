def is_float(in_value):
    """Checks if a value is a valid float.

    Parameters
    ----------
    in_value
        A variable of any type that we want to check is a float.

    Returns
    -------
    bool
        True/False depending on whether it was a float.

    Examples
    --------
    >>> is_float(1.5)
    True
    >>> is_float(1)
    False
    >>> is_float("1.5")
    True

    """
    try:
        return not float(in_value).is_integer()
    except (ValueError, TypeError):
        return False
