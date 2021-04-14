FAQ
===

Here's a list of commonly asked questions. If you can't find what you're looking for here you may
want to consider asking a question on `StackOverflow <https://stackoverflow.com/questions/tagged/python>`_.

Why should I use ``is-number``?
-------------------------------

You probably shouldn't! This project was built as part of a `blog post series on creating an open source Python project from scratch
<https://jacobtomlinson.dev/series/creating-an-open-source-python-project-from-scratch/>`_.

It contains a trivially small amount of code and is poking a bit of tongue-in-cheek fun at the JavaScript community
who are known for publishing very small packages on NPM and then having `half the internet break if one package is taken down
<https://www.theregister.com/2016/03/23/npm_left_pad_chaos/>`_.

If you want to check if something is a number in your Python code you should probably just write your own utility function
like this instead of adding another dependency.

.. code-block:: python

    def is_number(in_value):
        try:
            float(in_value)
            return True
        except (ValueError, TypeError):
            return False
