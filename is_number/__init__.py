"""Utility functions to calculate if an object is a number."""
from .is_number import is_number
from .is_float import is_float
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
