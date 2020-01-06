from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def is_number(in_value):
    try:
        float(in_value)
        return True
    except ValueError:
        return False

