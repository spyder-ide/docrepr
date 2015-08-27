# About

Docrepr is a library to render Python docstrings as html pages. It is based on
the `sphinxify` module developed by Tim Dumol for the Sage Notebook and the
`utils.inspector` one developed for Spyder.

# Details

The module renders dictionary as returned by IPython `oinspect` and exports
two functions - **sphinxify** which uses Sphinx to render docstrings, and
**rich_repr** that generates full HTML page with all assets from
`IPython.core.oinspect` output and returns URL to it. 

# License

This project is distributed under the under the terms of the Modified BSD
License
