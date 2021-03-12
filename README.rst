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

Developing
----------

This project uses ``black`` to format code and ``flake8`` for linting. We also support ``pre-commit`` to ensure
these have been run. To configure your local environment please install these development dependencies and set up
the commit hooks.

.. code-block:: bash

   $ pip install black flake8 pre-commit
   $ pre-commit install

Testing
-------

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block:: bash

   $ pip install -r requirements_test.txt

Run the tests.

.. code-block:: bash

   $ pytest
   === 3 passed in 0.13 seconds ===

Releasing
---------

Releases are published automatically when a tag is pushed to GitHub.

.. code-block:: bash

   # Set next version number
   export RELEASE=x.x.x

   # Create tags
   git commit --allow-empty -m "Release $RELEASE"
   git tag -a $RELEASE -m "Version $RELEASE"

   # Push
   git push upstream --tags