def is_number(in_value):
    try:
        float(in_value)
        return True
    except ValueError:
        return False