# About

Docrepr is a library to render Python docstrings as html pages. It is based on
the `sphinxify` module developed by Tim Dumol for the Sage Notebook and the
`utils.inspector` one developed for Spyder.

# Rationale

Video presentation @ SciPy 2015 by Carlos Cordoba:

[![Towards a Better Documentation System for Scientific Python | SciPy 2015 | Carlos Cordoba ](http://img.youtube.com/vi/q0r7FsDZU9s/0.jpg)](http://www.youtube.com/watch?v=q0r7FsDZU9s)

# Details

The module renders a dictionary as returned by IPython `oinspect` module and
exports two functions: `sphinxify` which uses Sphinx to render docstrings,
and `rich_repr` that generates full HTML page (with all assets) from
`IPython.core.oinspect` output and returns a URL to it.

Example:

    >>> import docrepr, IPython
    >>> myset = set()
    >>> oinfo = IPython.core.oinspect.Inspector().info(myset, oname='myset')
    >>> docrepr.sphinxify.rich_repr(oinfo)
    c:\users\user\appdata\local\temp\docrepr\tmpwvoj3s\rich_repr_output.html

`docrepr` can also show a window with rendered documentation of a docstring
if you have PyQt4 or PySide installed:

    >>> from docrepr import webview
    >>> s = set([1,2,3])
    >>> webview(s, oname='s')

`oname` is a just a name for the object, because Python loses it when
variable is passed to function.

# License

This project is distributed under the under the terms of the Modified BSD
License
