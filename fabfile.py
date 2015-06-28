# -*- coding: utf-8 -*

"""
Simple fabric file to test oinspect output
"""

from __future__ import print_function

import webbrowser

import oinspect.utils as utils
import oinspect.sphinxify as spxy

def _show_page(content, fname):
    with open(fname, 'wb') as f:
        f.write(utils.to_binary_string(content, encoding='utf-8'))
    webbrowser.open_new_tab(fname)

def test_basic():
    """Test with an empty context"""
    docstring = 'A test'
    content = spxy.sphinxify(docstring, spxy.generate_context())
    _show_page(content, '/tmp/test_basic.html')

def test_math():
    """Test a docstring with Latex on it"""
    docstring = 'This is a rational number :math:`\\frac{x}{y}`'
    content = spxy.sphinxify(docstring, spxy.generate_context())
    _show_page(content, '/tmp/test_math.html')

def test_numpy_sin():
    """Test for numpy.sin docstring"""
    import numpy as np
    docstring = np.sin.__doc__
    content = spxy.sphinxify(docstring, spxy.generate_context(name='sin'))
    _show_page(content, '/tmp/test_np_sin.html')

def run_all():
    """Run all tests"""
    test_basic()
    test_math()
    test_numpy_sin()
