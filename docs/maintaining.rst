Maintaining
===========

Reviewing Pull Requests
-----------------------

This project generally accepts any Pull Request which improves the project.

Any small issues which fix typos or improve documentation can be merged straight in.

Any bug fix or enhancement PRs should reference an open issue which describes the problem. This gives
us and other users the opportunity to discuss the change before anyone invests time in implementing it.

Typically we have a "yes and" policy when it comes to reviewing where we generally accept whatever is contributed even
if it's not quite right. If you have a small amount of feedback during review, such as the user forgot to run ``black`` or
you want to reword something in a docstring it's preferable to just push extra commits to the PR, or just merge
and raise a follow up PR to tweak things.

For larger design or implementation feedback then feel free to push this back on to the contributor.

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