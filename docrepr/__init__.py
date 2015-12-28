# -*- coding: utf-8 -*-
#
# Copyright (c) 2009 Tim Dumol
# Copyright (c) 2013- The Spyder Development team
#
# Licensed under the terms of the Modified BSD License

"""
Docrepr library

Library to generate rich and plain representations of docstrings,
including several metadata of the object to which the docstring
belongs

Derived from spyderlib.utils.inspector and IPython.core.oinspect
"""

__version__ = '0.0.1'

# Configuration options for docrepr
options = {
    'render_math': True,
    'local_mathjax': False,
    'collapse_sections': False,
    'use_qt4': False,
    'outline': False
}

# This imports IPython and PySide/PyQt4
# [ ] find a way to do delayed import
from .webview import webview

