opynions
========

|pypi-badge| |travis-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge|

Opynions inspects a code repository and warns the user if that repository
deviates from a selected set of opinions on how it should be organized.  It's
a good complement for a `cookiecutter`_; the cookiecutter provides a good
template for starting a repository with current best practices, and opynions
helps it keep up with those practices as they evolve over time.

Overview
--------

Opynions is effectively a static code analysis tool for the structure of a
software repository itself, rather than the source code within it.  It lets
the user select a set of opinions they (or their organization) agree with
about how a repository should be configured and what tools it should use.
Such options could include:

* pytest should be used as the test runner
* tox should be used to check compatibility with all supported Python versions
* Documentation should be built with Sphinx and hosted on Read the Docs
* pip-tools should be used to management requirements files, and there should
  be a few such files with standard names and roles
* pipenv should be used to manage requirements files and virtualenvs

The sets of opinions to enforce (and individual opinions within those sets to
ignore) are configured in an ``[opynions]`` section in ``setup.cfg``.  Each
individual opinion is a pytest test case, and each set of opinions is a
module of such test cases.  Common operations such as parsing configuration
files are handled by pytest fixtures, so individual opinion implementations
tend to be very concise:

* Is there a ``tox.ini`` file?
* Does it contain a ``[tox]`` section?
* Does the ``[tox]`` section contain ann

Documentation
-------------

The full documentation is at https://opynions.readthedocs.org.

License
-------

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.

Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for Open edX code in general.

The pull request description template should be automatically applied if you are creating a pull request from GitHub.  Otherwise you
can find it it at `PULL_REQUEST_TEMPLATE.md <https://github.com/edx/opynions/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_

The issue report template should be automatically applied if you are creating an issue on GitHub as well.  Otherwise you
can find it at `ISSUE_TEMPLATE.md <https://github.com/edx/opynions/blob/master/.github/ISSUE_TEMPLATE.md>`_

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _list of resources: https://open.edx.org/getting-help


.. |pypi-badge| image:: https://img.shields.io/pypi/v/opynions.svg
    :target: https://pypi.python.org/pypi/opynions/
    :alt: PyPI

.. |travis-badge| image:: https://travis-ci.org/edx/opynions.svg?branch=master
    :target: https://travis-ci.org/edx/opynions
    :alt: Travis

.. |codecov-badge| image:: http://codecov.io/github/edx/opynions/coverage.svg?branch=master
    :target: http://codecov.io/github/edx/opynions?branch=master
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/opynions/badge/?version=latest
    :target: http://opynions.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/opynions.svg
    :target: https://pypi.python.org/pypi/opynions/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/edx/opynions.svg
    :target: https://github.com/edx/opynions/blob/master/LICENSE.txt
    :alt: License
