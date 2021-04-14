is-number
=========

.. image:: https://img.shields.io/pypi/v/is-number
   :target: https://pypi.org/project/is-number/
   :alt: PyPI
.. image:: https://github.com/jacobtomlinson/is-number/workflows/CI/badge.svg
   :target: https://github.com/jacobtomlinson/is-number/actions?query=workflow%3ACI
   :alt: GitHub Actions - CI
.. image:: https://github.com/jacobtomlinson/is-number/workflows/pre-commit/badge.svg
   :target: https://github.com/jacobtomlinson/is-number/actions?query=workflow%3Apre-commit
   :alt: GitHub Actions - pre-commit
.. image:: https://img.shields.io/codecov/c/gh/jacobtomlinson/is-number
   :target: https://app.codecov.io/gh/jacobtomlinson/is-number
   :alt: Codecov

A Python library to determine if something is a number.

Installation
------------

.. code-block:: bash

   pip install is-number


Usage
-----

.. code-block:: python

   >>> from is_number import is_number
   >>> is_number(10)
   True
   >>> is_number("hello")
   False


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   faq