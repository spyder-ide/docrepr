# About

Docrepr is a library to render Python docstrings as html pages. It is based on
the `sphinxify` module developed by Tim Dumol for the Sage Notebook and the
`utils.inspector` one developed for Spyder.

# Details

The module renders dictionary as returned by IPython `oinspect` and exports
two functions - **sphinxify** which uses Sphinx to render docstrings, and
**rich_repr** that generates full HTML page (with all assets) from
`IPython.core.oinspect` output and returns URL to it.

Example:

    >>> import docrepr, IPython
    >>> myset = set()
    >>> oinfo = IPython.core.oinspect.Inspector().info(myset, oname='myset')
    >>> docrepr.sphinxify.rich_repr(oinfo)
    c:\users\user\appdata\local\temp\docrepr\tmpwvoj3s\rich_repr_output.html

# License

This project is distributed under the under the terms of the Modified BSD
License
