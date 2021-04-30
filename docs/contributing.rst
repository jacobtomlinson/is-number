Contributing
============

We love contributions here in ``is-number``! If you're looking for something to work on then check out our
`issue tracker <https://github.com/jacobtomlinson/is-number/issues>`_ for open issues.

If you want to make a contribution to ``is-number`` then please raise a
`Pull Request <https://github.com/jacobtomlinson/is-number/pulls>`_ on GitHub.

To help speed up the review process please ensure the following:

- The PR addresses an open issue.
- All tests are passing locally with ``pytest``.
- The project passes linting with ``black`` and ``flake8``.
- If adding a new feature you also add documentation.

Developing
----------

To check out a local copy of the project you can `fork the project on GitHub <https://github.com/jacobtomlinson/is-number/fork>`_
and then clone it locally.

.. code-block:: bash

   $ git clone git@github.com:yourusername/is-number.git
   $ cd is-number

This project uses ``black`` to format code and ``flake8`` for linting. We also support ``pre-commit`` to ensure
these have been run. To configure your local environment please install these development dependencies and set up
the commit hooks.

.. code-block:: bash

   $ pip install black flake8 pre-commit
   $ pre-commit install

You can check that things are working correctly by calling pre-commit directly.

.. code-block:: bash

   $ pre-commit run --all-files
   black......................................Passed
   flake8.....................................Passed

These checks will be run automatically when you make a commit.

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

If you are working on a new feature please add tests to ensure the feature works as expected. If you are working on
a bug fix then please add a test to ensure there is no regression.

Tests are stored in ``is_number/tests`` and follow the pytest format.

.. code-block:: python

    from is_number import is_number

    def test_is_number():
        assert is_number(1)
        assert not is_number("hello world!")

Making a Pull Request
---------------------

Once you've made your changes and are ready to make a Pull Request please ensure tests and linting pass locally before pushing to GitHub.
When making your Pull Request please include a short description of the changes, but more importantly why they are important. Perhaps by
writing a before and after paragraph with user examples.

Also consider how your title look when it appears in a changelog. Does it full describe the change to an outside user? For example
``Add support for checking iterables contain all numbers`` is a much better title than ``Fixes #76``.

.. code-block:: markdown

    # Add support for checking iterables contain all numbers

    Closes #56

    **Changes**

    This PR allows the inspection of structures such as lists and sets to check if all elements are numbers.

    **Before**

    If a user passed a list of all numbers to `is_number` it would return `False`.

    ```python
    >>> from is_number import is_number
    >>> is_number([0,1,2])
    False
    ```

    **After**

    If a user passes a list of all numbers it will return true, unless they set the `strict` keyword argument to `True`.


    ```python
    >>> from is_number import is_number
    >>> is_number([0,1,2])
    True
    >>> is_number([0,1,2], strict=True)
    False
    ```
