# Copyright (c) 2009 Tim Dumol
# Copyright (c) 2013- The Spyder Development Team and Docrepr Contributors
#
# Distributed under the terms of the BSD BSD 3-Clause License

"""
Docrepr
=======

Library to generate rich and plain representations of docstrings,
including several metadata of the object to which the docstring
belongs.

Derived from spyderlib.utils.inspector and IPython.core.oinspect.
"""

__version__ = '0.2.1.dev0'

# Configuration options for docrepr
options = {
    'render_math': True,
    'local_mathjax': False,
    'collapse_sections': False,
    'use_qt4': False,
    'outline': False
}
